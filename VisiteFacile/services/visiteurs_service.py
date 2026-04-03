
from VisiteFacile.utils.connect import visiteurs
from bson import ObjectId
import csv, io
import VisiteFacile.dtos.VisiteurDTO as DTO
import VisiteFacile.repo.requete as repo



def add_visiteur(dto: DTO.VisiteurDTO):
    insert = dto.to_mongo_dict()
    repo.add_visiteur(insert)


def trouver_visiteurs(query: dict, limit, page):
    return repo.trouver_visiteur(query, limit, page)



def del_visiteur(visiteur_id : str):
    result = visiteurs.delete_one({"_id": ObjectId(visiteur_id)})
    return result

def get_visiteurs(page: int,  limit: int):
    return repo.get_visiteurs(page, limit)


def get_infos(visiteur_id: str):
    return repo.get_infos(visiteur_id)




def update_visiteur(dto: DTO.UpdateVisiteurDTO, visiteur_id: str):
    update = dto.to_mongo_dict()
    visiteur = get_infos(visiteur_id)
    visiteur_object_id = ObjectId(visiteur["_id"])
    repo.update_visiteur(visiteur_object_id, update)



def get_export(args):
    query = get_filtres(args)

    documents = repo.get_visiteurs_avec_filtre(query)

    if not documents:
        return None

    champs = ["nom", "prenom", "date_naissance", "mail", "ville", "etablissement",
                "departement_visite", "bac", "specialite_1", "specialite_2",
                "filiere", "reorientation", "immersion", "evenement", "autre"]

    fichier = io.StringIO()
    writer = csv.DictWriter(fichier, fieldnames=champs, delimiter=";")
    writer.writeheader()
    writer.writerows(documents)
    fichier.seek(0)

    return fichier

def get_filtres(args):
    champs_textuels = ["ville", "etablissement", "departement_visite", "bac", "specialite_1", "specialite_2", "filiere", "evenement"]
    champs_booleens = ["reorientation", "immersion"]

    filtres = {}

    ## Permet de récupérer les filtres textuels
    for f in champs_textuels:
        value = args.get(f)
        if value:
            filtres[f] = {"$regex": value, "$options": "i"}

    ## Permet de récupérer les filtres booleens
    for f in champs_booleens:
        value = args.get(f)
        if value == "true":
            filtres[f] = True

    return filtres