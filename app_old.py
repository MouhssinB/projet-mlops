# prompt: Création de l'API : A l'aide de Flask, exposer le modèle en déployant, en local, une API qui recevra les données des clients en entrée et renverra une prédiction (churn ou non churn).

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'data/model.pickle')

@app.route('/predict', methods=['POST'])
def predict():
  """
  Endpoint to predict churn based on client data.

  Expects a JSON payload with client features.
  """
  try:
    data = request.get_json()

    # Ensure that the required features are present in the JSON
    required_features = ['Age', 'Account_Manager', 'Years', 'Num_Sites']
    if not all(feature in data for feature in required_features):
      return jsonify({'error': 'Missing required features'}), 400

    # Extract features from the JSON data
    features = [data['Age'], data['Account_Manager'], data['Years'], data['Num_Sites']]

    # Make prediction using the loaded model
    prediction = model.predict([features])[0]

    # Return the prediction as a JSON response
    return jsonify({'churn_prediction': int(prediction)})  # Convert to int for consistency

  except Exception as e:
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True)  # Run the Flask app in debug mode
