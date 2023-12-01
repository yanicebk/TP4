def nombre_plus_frequent(liste):
    # Utilisation de dictionnaire pour compter les occurrences de chaque élément
    occurrences = {}

    for nombre in liste:
        if nombre in occurrences:
            occurrences[nombre] += 1
        else:
            occurrences[nombre] = 1

    # Trouver l'élément avec le plus grand nombre d'occurrences
    nombre_frequent = max(occurrences, key=occurrences.get)
    occurrences_max = occurrences[nombre_frequent]

    # Afficher le résultat
    print(f"Le nombre le plus fréquent dans la liste est le : {nombre_frequent} ({occurrences_max} x)")


# Exemple d'utilisation avec la liste L1
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
nombre_plus_frequent(L1)
