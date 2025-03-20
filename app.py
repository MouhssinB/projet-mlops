from flask import Flask, request, jsonify, make_response
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'data/model.pickle')
@app.route('/')
def home():
    return "Bienvenue sur l'API de prédiction de churn !", 200


@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
  """
  Endpoint to predict churn based on client data.
  
  Accepts form data with client features.
  """
  # Handle preflight OPTIONS request for CORS
  if request.method == 'OPTIONS':
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response
    
  try:
    # Get form data
    age = float(request.form.get('Age'))
    account_manager = int(request.form.get('Account_Manager'))
    years = float(request.form.get('Years'))
    num_sites = int(request.form.get('Num_Sites'))
    
    # Ensure all required features are provided
    if None in [age, account_manager, years, num_sites]:
      return jsonify({'error': 'Missing required features'}), 400
    
    # Create a DataFrame with the same feature names used during training
    features_df = pd.DataFrame([[age, account_manager, years, num_sites]], 
                              columns=['Age', 'Account_Manager', 'Years', 'Num_Sites'])
    
    # Make prediction using the loaded model
    prediction = model.predict(features_df)[0]
    
    # Create the response with CORS headers
    response = jsonify({'churn_prediction': int(prediction)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  
  except ValueError as ve:
    response = jsonify({'error': f'Invalid data format: {str(ve)}'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 400
  
  except Exception as e:
    response = jsonify({'error': str(e)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 500

if __name__ == '__main__':
  app.run(debug=True)  # Run the Flask app in debug mode