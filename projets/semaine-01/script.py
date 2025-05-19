import os
import time
from datetime import datetime

# Paramètres
chemin = "."  # dossier à parcourir (modifiable)
seuil_heures = 24  # durée en heures

# Calcul du seuil en secondes
seuil_secondes = seuil_heures * 3600
maintenant = time.time()

print(f"Fichiers modifiés dans les {seuil_heures} dernières heures :\n")

for root, dirs, files in os.walk(chemin):
    for fichier in files:
        chemin_complet = os.path.join(root, fichier)
        if os.path.isfile(chemin_complet):
            modif = os.path.getmtime(chemin_complet)
            if maintenant - modif < seuil_secondes:
                date_lisible = datetime.fromtimestamp(modif).strftime('%Y-%m-%d %H:%M:%S')
                print(f"{chemin_complet} (modifié le {date_lisible})")
