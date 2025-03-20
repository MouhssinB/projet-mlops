import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



df_cust = pd.read_csv(r"data/customer_churn.csv")
df_cust_1 = df_cust[['Age' , 'Total_Purchase' , 'Account_Manager' , 'Years' ,'Num_Sites', 'Churn']].copy()


# Split the data into training and testing sets
X = df_cust_1.drop(['Churn' , 'Total_Purchase'], axis=1)  # Features
y = df_cust_1['Churn']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

# Créez une instance du modèle de régression logistique
model_2 = LogisticRegression()

# Entraînez le modèle sur les données d'entraînement
model_2.fit(X_train, y_train)

# Faites des prédictions sur l'ensemble de test
y_pred = model_2.predict(X_test)


# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

# Print the results
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
print(f"ROC AUC: {roc_auc}")

import joblib
joblib.dump(model_2, r'data/model.pickle')
