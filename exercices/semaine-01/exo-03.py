# Exercice 3 : Moyenne de notes
# - Calcule la moyenne d'une liste de notes
# - Affiche une mention selon la moyenne

notes = [12, 15, 10, 17, 14]
moyenne = sum(notes) / len(notes)
print("Moyenne :", moyenne)

if moyenne < 10:
    print("Insuffisant")
elif moyenne < 14:
    print("Passable")
elif moyenne < 17:
    print("Bien")
else:
    print("Très bien")
