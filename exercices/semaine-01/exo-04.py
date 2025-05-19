# Exercice 4 : Parcours de fichier

# ✅ Exemple guidé :
import os

chemin = "."
for root, dirs, files in os.walk(chemin):
    for fichier in files:
        if fichier.endswith(".txt"):
            print(os.path.join(root, fichier))
            print(f"{os.path.getsize(fichier)} octets")

# 🎯 À toi de jouer :
# Modifie ce programme pour :
# - Afficher uniquement les fichiers `.txt`
# - Afficher aussi leur taille (en octets)
# 💡 Indice : `os.path.getsize(fichier)`
