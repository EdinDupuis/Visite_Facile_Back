from VisiteFacile.utils.connect import visiteurs
from bson import ObjectId
import VisiteFacile.dtos.VisiteurDTO as DTO
import VisiteFacile.repo.requete as repo


def add_visiteur(dto: DTO.VisiteurDTO):
    insert = dto.to_mongo_dict()
    repo.add_visiteur(insert)


def trouver_visiteurs(query: dict, limit, page):
    return repo.trouver_visiteur(query, limit, page)


def get_visiteurs(page: int,  limit: int):
    return repo.get_visiteurs(page, limit)


def get_infos(visiteur_id: str):
    return repo.get_infos(visiteur_id)



def update_visiteur(dto: DTO.UpdateVisiteurDTO, visiteur_id: str):
    update = dto.to_mongo_dict()
    visiteur = get_infos(visiteur_id)
    visiteur_object_id = ObjectId(visiteur["_id"])
    repo.update_visiteur(visiteur_object_id, update)

