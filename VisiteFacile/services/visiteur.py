class Visiteur:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom

    def get_id(self):
        return self.id

    def get_nom(self):
        return self.nom