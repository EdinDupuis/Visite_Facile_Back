class VisiteurDTO:
    def __init__(self, prenom, nom, mail, date_naissance, specialite_1,
                 specialite_2,bac, reorientation, departement_visite,
                 ville, etablissement, immersion, evenement, autre=None):

        self.prenom = prenom
        self.nom = nom
        self.mail = mail
        self.date_naissance = date_naissance
        self.bac = bac
        self.specialite_1 = specialite_1
        self.specialite_2 = specialite_2
        self.reorientation = reorientation
        self.departement_visite = departement_visite
        self.ville = ville
        self.etablissement = etablissement
        self.immersion = immersion
        self.evenement = evenement
        self.autre = autre

