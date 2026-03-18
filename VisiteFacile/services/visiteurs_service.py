from utils.connect import visiteurs
def add_visiteur(visiteur: dict):
    visiteurs.insert_one(visiteur)

def trouver_visiteurs(query: dict):
    visiteurs_list = list(visiteurs.find(query))
    for v in visiteurs_list:
        v["_id"] = str(v["_id"])
    return visiteurs_list