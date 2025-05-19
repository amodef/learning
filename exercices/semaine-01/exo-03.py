# Exercice 3 : Moyenne de notes

# ✅ Exemple guidé :
notes = []

i = 0
while i < 3:
	notes.append(float(input(f"Insérer la note {i+1} : ")))
	i += 1

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

# 🎯 À toi de jouer :
# Demande à l’utilisateur de saisir 3 notes (via `input()`)
# puis calcule et affiche la moyenne et la mention
# 💡 Indice : utilise `float(input(...))` et une liste
