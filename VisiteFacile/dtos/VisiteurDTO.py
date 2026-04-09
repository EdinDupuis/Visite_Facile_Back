from typing import Optional

from pydantic import BaseModel


class BaseDTO(BaseModel):
    def to_mongo_dict(self):
        res = self.model_dump(exclude_none=True)

        res = {k: v for k, v in res.items() if v not in [None, "", False]}
        if "id" in res:
            res["_id"] = res.pop("id")
        return res


class CreateVisiteurDTO(BaseDTO):
    prenom: str
    nom: str
    mail: str
    date_naissance: str
    bac: str
    specialite_1: str
    specialite_2: str
    filiere: Optional[str] = None
    reorientation: Optional[bool] = False
    departement_visite: str
    ville: str
    etablissement: str
    immersion: Optional[bool] = False
    evenement: str
    situation_particuliere: Optional[bool] = False
    autre: Optional[str] = None


class UpdateVisiteurDTO(BaseDTO):
    prenom: Optional[str] = None
    nom: Optional[str] = None
    mail: Optional[str] = None
    date_naissance: Optional[str] = None
    bac: Optional[str] = None
    specialite_1: Optional[str] = None
    specialite_2: Optional[str] = None
    filiere: Optional[str] = None
    reorientation: Optional[bool] = None
    departement_visite: Optional[str] = None
    ville: Optional[str] = None
    etablissement: Optional[str] = None
    immersion: Optional[bool] = None
    evenement: Optional[str] = None
    situation_particuliere: Optional[bool] = None
    autre: Optional[str] = None

