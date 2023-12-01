nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []

for i in range(nombreEtudiants):
    note = float(input(f"Note étudiant {i} : "))
    while not (0 <= note <= 20):
        print("La note doit être comprise entre 0 et 20.")
        note = float(input(f"Entrez à nouveau la note étudiant {i} : "))
    notes.append(note)

moyenne = sum(notes) / nombreEtudiants

print(f"Moyenne de classe : {moyenne:.2f}")
print("Numéro de l’Étudiant | Note | Écart à la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note} | {ecart:.2f}")
