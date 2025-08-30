# 1. Image de base
FROM python:3.12-slim

# 2. Définir le répertoire de travail dans le container
WORKDIR /app

# 3. Copier les fichiers nécessaires
COPY requirements.txt .
COPY . .

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Exposer le port que FastAPI va utiliser
EXPOSE 8000

# 6. Définir la commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
