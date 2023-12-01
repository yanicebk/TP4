nMax = 3

n = int(input(f"Entrez la taille des vecteurs (entre 1 et {nMax} inclus) : "))
while not (1 <= n <= nMax):
    n = int(input(f"Entrez à nouveau la taille des vecteurs : "))

v1 = [int(input(f"v1[{i}] : ")) for i in range(n)]
v2 = [int(input(f"v2[{i}] : ")) for i in range(n)]

produit_scalaire = sum(v1[i] * v2[i] for i in range(n))

print(f"Le produit scalaire de v1 et v2 est : {produit_scalaire}")
