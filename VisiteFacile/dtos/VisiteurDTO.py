from pydantic import BaseModel, ConfigDict

class BaseDTO(BaseModel):
    def to_mongo_dict(self):
        res = {}
        for key, value in __dict__.items():
            if value not in [None, '']:
                if key == "id":
                    res["_id"] = value
                else:
                    res[key] = value
        return res

class VisiteurDTO(BaseDTO):
        id : str
        prenom : str
        nom : str
        mail : str
        date_naissance : str
        bac : str
        specialite_1 : str
        specialite_2 : str
        filiere : str
        reorientation : bool
        departement_visite : str
        ville : str
        etablissement : str
        immersion : bool
        evenement : str
        autre : str

class UpdateVisiteurDTO(BaseDTO):
        prenom : str
        nom : str
        mail : str
        date_naissance : str
        bac : str
        specialite_1 : str
        specialite_2 : str
        filiere : str
        reorientation : bool
        departement_visite : str
        ville : str
        etablissement : str
        immersion : bool
        autre : str


class GetVisiteurDTO(BaseDTO):
        _id : str
        nom : str
        prenom : str
        date_naissance : str
        ville : str
        departement_visite : str




