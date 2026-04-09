from VisiteFacile.utils.connect import visiteurs
from bson import ObjectId
import csv, io
import VisiteFacile.dtos.VisiteurDTO as DTO
import VisiteFacile.repo.requete as repo


def add_visiteur(dto: DTO.CreateVisiteurDTO):
    insert = dto.to_mongo_dict()
    repo.add_visiteur(insert)

def get_all(query):
    return repo.get_all(query)

def trouver_visiteurs(query: dict, page, limit):
    return repo.trouver_visiteur(query, page, limit)


def del_visiteur(visiteur_id: str):
    result = visiteurs.delete_one({"_id": ObjectId(visiteur_id)})
    return result


def get_visiteurs(page: int, limit: int):
    return repo.get_visiteurs(page, limit)


def get_infos(visiteur_id: str):
    return repo.get_infos(visiteur_id)


def update_visiteur(dto: DTO.UpdateVisiteurDTO, visiteur_id: str):
    visiteur = get_infos(visiteur_id)
    if not visiteur:
        return None
    update = dto.to_mongo_dict()
    visiteur_object_id = ObjectId(visiteur["_id"])
    repo.update_visiteur(visiteur_object_id, update)
    return True


def get_export(args):
    query = get_filtres(args)

    documents = repo.get_visiteurs_avec_filtre(query)

    if not documents:
        return None

    champs = ["nom", "prenom", "date_naissance", "mail", "ville", "etablissement",
              "departement_visite", "bac", "specialite_1", "specialite_2",
              "filiere", "reorientation", "immersion", "evenement", "situation_particuliere", "autre"]

    fichier = io.StringIO()
    writer = csv.DictWriter(fichier, fieldnames=champs, delimiter=";", extrasaction="ignore")
    writer.writeheader()
    for doc in documents:
        row = {champ: doc.get(champ, "") for champ in champs}
        writer.writerow(row)
    fichier.seek(0)

    return fichier


def get_filtres(args):
    champs_textuels = ["nom", "prenom", "date_naissance", "ville", "etablissement", "departement_visite", "bac", "specialite_1", "specialite_2", "filiere",
                       "evenement"]
    champs_booleens = ["reorientation", "immersion", "situation_particuliere"]

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
