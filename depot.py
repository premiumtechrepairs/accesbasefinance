
from db import get_connection
from modeles import Societes


# 1. Rechercher une societe par son ID
def get_societe_by_id(id):
    connexion = get_connection()

    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                """
                SELECT id, nom, symbole, secteur, pays
                FROM societes
                WHERE id = %s
                """,
                (id,)
            )

            ligne = curseur.fetchone()

            if ligne is None:
                return None

            return Societe(**ligne)

    finally:
        connexion.close()


# 2. Lister toutes les societes
def lister_societes():
    connexion = get_connection()

    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                """
                SELECT id, nom, symbole, secteur, pays
                FROM societes
                ORDER BY nom
                """
            )

            lignes = curseur.fetchall()

            return [Societes(**ligne) for ligne in lignes]

    finally:
        connexion.close()


# 3. Ajouter une societe
def ajouter_societe(nom, symbole, secteur, pays):
    connexion = get_connection()

    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                """
                INSERT INTO societes
                (nom, symbole, secteur, pays)
                VALUES (%s, %s, %s, %s)
                """,
                (nom, symbole, secteur, pays)
            )

            nouvel_id = curseur.lastrowid

        connexion.commit()

        return get_societe_by_id(nouvel_id)

    except Exception:
        connexion.rollback()
        raise

    finally:
        connexion.close()


# 4. Supprimer une societe par son nom
def supprimer_societe(nom):
    connexion = get_connection()

    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                """
                DELETE FROM societes
                WHERE nom = %s
                """,
                (nom,)
            )

            nombre_supprime = curseur.rowcount

        connexion.commit()

        return nombre_supprime

    except Exception:
        connexion.rollback()
        raise

    finally:
        connexion.close()
