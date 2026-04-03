from typing import List

import dtos.VisiteurDTO as DTO
from utils.connect import visiteurs
from bson import ObjectId


def add_visiteur(insert):
    result = visiteurs.insert_one(insert)


def trouver_visiteur(query: dict, page, limit):
    if len(query) != 0:
        visiteurs_list = list(visiteurs.find(query).skip((page - 1) * limit).limit(limit))
    else:
        visiteurs_list = get_visiteurs(page, limit)
    if visiteurs_list is not None:
        for v in visiteurs_list:
            v["_id"] = str(v["_id"])


    return visiteurs_list


def get_visiteurs(page: int, limit: int):
    users = list(visiteurs.find({}, {"_id": 1, "nom": 1, "prénom": 1, "date_naissance": 1, "ville": 1,
                                     "departement_visite": 1}).skip((page - 1) * limit).limit(limit))

    for user in users:
        user["_id"] = str(user["_id"])

    return users


def get_infos(visiteur_id):
    infos = visiteurs.find_one({"_id": ObjectId(visiteur_id)})

    if infos:
        infos["_id"] = str(infos["_id"])

    return infos


def update_visiteur(visiteur_id: ObjectId, update: dict):
    visiteurs.update_one({"_id": visiteur_id}, {"$set": update})


def get_visiteurs_avec_filtre(query):
    return list(visiteurs.find(query, {"_id": 0}))
