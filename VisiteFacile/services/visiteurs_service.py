from utils.connect import visiteurs
def add_visiteur(visiteur: dict):
    visiteurs.insert_one(visiteur)

def trouver_visiteur_par_nom(visiteur_nom):
    visiteurs_list = list(visiteurs.find({'nom': visiteur_nom}))
    for v in visiteurs_list:
        v["_id"] = str(v["_id"])
    return visiteurs_list