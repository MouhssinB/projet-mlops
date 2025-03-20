import tkinter as tk
from tkinter import messagebox
import requests

def call_api():
    url = 'http://127.0.0.1:5000/predict'  # Remplacez par l'URL de votre API
    
    try:
        data = {
            'Age': int(entry_age.get()),
            'Account_Manager': int(entry_account_manager.get()),
            'Years': int(entry_years.get()),
            'Num_Sites': int(entry_num_sites.get())
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            result = response.json()
            messagebox.showinfo("Résultat", f"Réponse de l'API : {result}")
        else:
            messagebox.showerror("Erreur", f"Erreur lors de l'appel à l'API : {response.status_code}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Appel API Predict")
root.geometry("300x250")

# Création des champs de saisie
labels = ["Age", "Account Manager", "Years", "Num Sites"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_age, entry_account_manager, entry_years, entry_num_sites = entries

# Bouton pour appeler l'API
tk.Button(root, text="Envoyer", command=call_api).grid(row=len(labels), column=0, columnspan=2, pady=10)

# Lancer la boucle principale
root.mainloop()
