from utils.connect import visiteurs
def add_visiteur(visiteur: dict):
    visiteurs.insert_one(visiteur)

def get_visiteurs():
    users = list(visiteurs.find({}, {"_id": 0, "nom": 1, "prénom": 1, "date_naissance": 1, "ville": 1, "département_visité": 1}))
    return users


