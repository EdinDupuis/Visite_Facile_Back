class VisiteurDTO:
    def __init__(self, prenom, nom, mail=None, date_naissance=None, specialite_1=None,
                 specialite_2=None,filiere=None,bac=None, reorientation=None, departement_visite=None,
                 ville=None, etablissement=None, immersion=None, evenement=None, autre=None):

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



    def to_mongo_dict(self): # Sert à "purger" les champs où y'a None '' ou False, comme ça on insère pas des données parasite dans la BD
        res = {}
        for key, value in self.__dict__.items():
            if value not in [None, '', False]:
                res[key] = value
        return res
