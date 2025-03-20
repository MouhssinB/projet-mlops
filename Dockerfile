# Utiliser une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY app.py .
COPY train.py .
COPY test_app.py .
COPY test_train.py .
COPY data/customer_churn.csv ./data/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter le script d'entraînement
RUN python train.py 

# Installer pytest
#RUN pip install pytest pytest-mock

# Exécuter les tests en premier
#RUN pytest test_train.py test_app.py -v

# Exposer le port pour Flask
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"] 