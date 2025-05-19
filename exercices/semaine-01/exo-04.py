# Exercice 4 : Parcours de fichier
# Parcourt tous les fichiers du dossier courant et affiche ceux qui se terminent par .py

import os

chemin = "."
for root, dirs, files in os.walk(chemin):
    for fichier in files:
        if fichier.endswith(".py"):
            print(os.path.join(root, fichier))
