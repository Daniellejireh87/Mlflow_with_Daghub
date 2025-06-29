# Utilise une image officielle Python
FROM python:3.10-slim

# Crée un dossier de travail
WORKDIR /app

# Copie les fichiers
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port de l'API
EXPOSE 5001

# Lance l’API Flask
CMD ["python", "serve_model.py"]
