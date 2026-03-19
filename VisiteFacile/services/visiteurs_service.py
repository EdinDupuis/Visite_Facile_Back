from utils.connect import visiteurs
def add_visiteur(visiteur: dict):
    visiteurs.insert_one(visiteur)

def trouver_visiteurs(query: dict, limit, page):
    skip = (page - 1) * limit
    visiteurs_cursor = visiteurs.find(query).skip(skip).limit(limit)
    visiteurs_list = list(visiteurs_cursor)
    for v in visiteurs_list:
        v["_id"] = str(v["_id"])

    return visiteurs_list