def table_multiplication(nombre):
    resultat_table = []

    for i in range(10):
        resultat = nombre * i
        resultat_table.append(resultat)

    print(f"Vous cherchez la table de multiplication de quel nombre ? {nombre}")
    for i, resultat in enumerate(resultat_table):
        print(f"{nombre} * {i} = {resultat:.1f}")

nombre_entre = float(input("Entrez le nombre pour lequel vous souhaitez la table de multiplication : "))

table_multiplication(nombre_entre)
