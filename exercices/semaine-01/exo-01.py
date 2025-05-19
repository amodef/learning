# Exercice 1 : Lister les fichiers modifiés récemment dans un dossier
import os
import time

# Chemin du dossier à analyser
dossier = "."

# Durée (en secondes) pour considérer un fichier comme "modifié récemment"
seuil = 24 * 3600  # 24 heures

now = time.time()

for root, dirs, files in os.walk(dossier):
    for file in files:
        chemin = os.path.join(root, file)
        if os.path.isfile(chemin):
            mtime = os.path.getmtime(chemin)
            if now - mtime < seuil:
                print(f"Modifié récemment : {chemin}")
