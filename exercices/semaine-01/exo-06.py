# Exercice 6 : Affichage avec délai
# Affiche : "Chargement ." -> "Chargement .." -> "Chargement ..." avec 1s d'attente

import time

for i in range(1, 4):
    print("Chargement" + "." * i)
    time.sleep(1)
