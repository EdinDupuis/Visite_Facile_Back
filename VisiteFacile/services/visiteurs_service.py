from bson import ObjectId

from utils.connect import visiteurs

from dtos import VisiteurDTO

def add_visiteur(dto: VisiteurDTO):
    insert = dto.to_mongo_dict()
    result = visiteurs.insert_one(insert)


def trouver_visiteurs(query: dict, limit, page):
    skip = (page - 1) * limit
    visiteurs_cursor = visiteurs.find(query).skip(skip).limit(limit)
    visiteurs_list = list(visiteurs_cursor)
    for v in visiteurs_list:
        v["_id"] = str(v["_id"])

    return visiteurs_list

def get_visiteurs():
    users = list(visiteurs.find({}, {"_id": 1, "nom": 1, "prenom": 1, "date_naissance": 1, "ville": 1, "département_visité": 1}))
    for user in users:
        user["_id"] = str(user["_id"])
    return users

def del_visiteur(visiteur_id : str):
    result = visiteurs.delete_one({"_id": ObjectId(visiteur_id)})
    return result

