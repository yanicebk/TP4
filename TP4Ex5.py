def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verification_date(date_str):
    if len(date_str) != 8:
        print("La date n'est pas au bon format. Veuillez entrer une date au format jjmmaaaa.")
        return

    jour, mois, annee = int(date_str[:2]), int(date_str[2:4]), int(date_str[4:])
    jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if jour < 1 or mois < 1 or mois > 12 or annee < 1:
        print("La date est incorrecte. Veuillez vérifier le jour, le mois et l'année.")
    elif jour > jours_par_mois[mois] + (mois == 2 and est_bissextile(annee)):
        print("La date est incorrecte. Le mois spécifié n'a pas autant de jours.")
    else:
        print("La date est valide.")


# Tester le programme avec les dates fournies
dates_a_tester = ["31021999", "31041000", "32052020", "30032021", "29022022"]

for date in dates_a_tester:
    print(f"\nVérification de la date {date}:")
    verification_date(date)
