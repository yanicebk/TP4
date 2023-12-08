# 1. Enregistrement des logins dans un tuplet nommé "binome"
binome = ('login1', 'login2')

# Affichage des membres du binôme
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

# 2. Changement de binôme en demandant un nouveau login
nouveau_login = input("Entrez le nouveau login : ")
binome = (binome[0], nouveau_login)

# Affichage des membres du nouveau binôme
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

# 3. Ajout d'un troisième élément au tuplet "binome" pour former un trinôme
troisieme_login = input("Entrez le troisième login : ")
binome += (troisieme_login,)

# Affichage des membres du trinôme
print(f"L'étudiant {binome[0]} est en trinôme avec les étudiants {binome[1]} et {binome[2]}")
