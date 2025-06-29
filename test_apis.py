import requests
from sklearn.datasets import load_digits

# Charger les données
digits = load_digits()
X = digits.data  # chaque ligne représente une image 8x8 = 64 pixels
y = digits.target

# Sélectionner quelques exemples à tester
# Par exemple les 3 premières images avec leurs vraies étiquettes
data = {
    "inputs": X[:3].tolist()
}

# Faire une requête POST à l'API
response = requests.post("http://127.0.0.1:5001/predict", json=data)

# Afficher les prédictions et les vraies étiquettes
if response.ok:
    predictions = response.json()
    print("✅ Prédictions :", predictions)
    print("🎯 Étiquettes attendues :", y[:3].tolist())
else:
    print("❌ Erreur :", response.status_code)
    print(response.text)
