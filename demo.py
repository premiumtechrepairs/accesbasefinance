
from depot import (
    get_societe_by_id,
    lister_societes,
    ajouter_societe,
    supprimer_societe
)


def main():

    while True:

        print("\n===== GESTION DES SOCIETES =====")
        print("1. Lister les societes")
        print("2. Rechercher une societe")
        print("3. Ajouter une societe")
        print("4. Supprimer une societe")
        print("5. Quitter")

        choix = input("\nVotre choix : ")

        # 1. Lister les societes
        if choix == "1":

            societes = lister_societes()

            print("\n--- LISTE DES SOCIETES ---")

            for societe in societes:
                print("--------------------")
                print("ID :", societe.id)
                print("Nom :", societe.nom)
                print("Symbole :", societe.symbole)
                print("Secteur :", societe.secteur)
                print("Pays :", societe.pays)

        # 2. Rechercher une societe
        elif choix == "2":

            id_societe = int(input("ID de la societe : "))

            societe = get_societe_by_id(id)

            if societe is None:
                print("Societe introuvable.")

            else:
                print("\n--- SOCIETE TROUVEE ---")
                print("ID :", societe.id)
                print("Nom :", societe.nom)
                print("Symbole :", societe.symbole)
                print("Secteur :", societe.secteur)
                print("Pays :", societe.pays)

        # 3. Ajouter une societe
        elif choix == "3":

            print("\n--- AJOUTER UNE SOCIETE ---")

            nom = input("Nom : ")
            symbole = input("Symbole boursier : ")
            secteur = input("Secteur : ")
            pays = input("Pays : ")

            societe = ajouter_societe(
                nom,
                symbole,
                secteur,
                pays
            )

            print("\nSociete ajoutee avec succes !")
            print("ID :", societe.id)
            print("Nom :", societe.nom)

        # 4. Supprimer une societe
        elif choix == "4":

            print("\n--- SUPPRIMER UNE SOCIETE ---")

            nom = input("Nom de la societe a supprimer : ")

            confirmation = input(
                "Confirmer la suppression ? (oui/non) : "
            )

            if confirmation.lower() == "oui":

                resultat = supprimer_societe(nom)

                if resultat > 0:
                    print(resultat, "societe(s) supprimee(s).")

                else:
                    print("Aucune societe trouvee.")

            else:
                print("Suppression annulee.")

        # 5. Quitter
        elif choix == "5":

            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
