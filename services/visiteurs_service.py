from utils.connect import visiteurs
from dtos import VisiteurDTO

def add_visiteur(dto: VisiteurDTO):
    insert = dto.to_mongo_dict()
    result = visiteurs.insert_one(insert)

