class BaseDTO:
    def to_mongo_dict(self):
        res = {}
        for key, value in self.__dict__.items():
            if value not in [None, '']:
                if key == "id":
                    res["_id"] = value
                else:
                    res[key] = value
        return res

class VisiteurDTO(BaseDTO):
    def __init__(self, id, prenom, nom, mail, date_naissance, specialite_1,
                 specialite_2, filiere, bac, reorientation, departement_visite,
                 ville, etablissement, immersion, evenement, autre):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.mail = mail
        self.date_naissance = date_naissance
        self.bac = bac
        self.specialite_1 = specialite_1
        self.specialite_2 = specialite_2
        self.filiere = filiere
        self.reorientation = reorientation
        self.departement_visite = departement_visite
        self.ville = ville
        self.etablissement = etablissement
        self.immersion = immersion
        self.evenement = evenement
        self.autre = autre

class UpdateVisiteurDTO(BaseDTO):
    def __init__(self, prenom, nom, mail, date_naissance, specialite_1,
                 specialite_2, filiere, bac, reorientation, departement_visite,
                 ville, etablissement, immersion, autre):
        self.prenom = prenom
        self.nom = nom
        self.mail = mail
        self.date_naissance = date_naissance
        self.bac = bac
        self.specialite_1 = specialite_1
        self.specialite_2 = specialite_2
        self.filiere = filiere
        self.reorientation = reorientation
        self.departement_visite = departement_visite
        self.ville = ville
        self.etablissement = etablissement
        self.immersion = immersion
        self.autre = autre



