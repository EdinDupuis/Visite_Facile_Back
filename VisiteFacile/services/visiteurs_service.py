from VisiteFacile.utils.connect import visiteurs
from bson import ObjectId
from VisiteFacile.dtos.VisiteurDTO import *


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
    users = list(
        visiteurs.find({}, {"_id": 1, "nom": 1, "prénom": 1, "date_naissance": 1, "ville": 1, "département_visité": 1}))

    for user in users:
        user["_id"] = str(user["_id"])
    return users


def get_infos(visiteur_id: str):
    infos = visiteurs.find_one({"_id": ObjectId(visiteur_id)})

    if infos:
        infos["_id"] = str(infos["_id"])
    return infos


def update_visiteur(dto: UpdateVisiteurDTO, visiteur_id: str):
    update = dto.to_mongo_dict()
    visiteur = get_infos(visiteur_id)
    visiteur_id = ObjectId(visiteur["_id"]) # besoin de caster en ObjectId sinon matchedCount retournera toujours 0 et donc on trouvera jamais le visiteur avec l'id X.
    result = visiteurs.update_one({"_id": visiteur_id}, {"$set": update})
