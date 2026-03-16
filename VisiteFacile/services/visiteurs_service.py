from utils.connect import visiteurs
def add_visiteur(visiteur: dict):
    visiteurs.insert_one(visiteur)

