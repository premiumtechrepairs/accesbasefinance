from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Societes:
    id: int
    nom: str
    symbole: str
    secteur: str
    pays: str


@dataclass
class Bilans:
    id: int
    societe_id: int
    annee: int
    chiffre_affaires: Decimal
    resultat_net: Decimal
    actifs_courants: Decimal
    passifs_courants: Decimal
    dettes_totales: Decimal
    capitaux_propres: Decimal
    total_actifs: Decimal


@dataclass
class Cours:
    id: int
    societe_id: int
    date_cours: date
    cours_cloture: Decimal
    volume: int