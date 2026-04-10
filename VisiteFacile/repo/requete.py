from typing import List

import VisiteFacile.dtos.VisiteurDTO as DTO
from VisiteFacile.utils.connect import visiteurs
from bson import ObjectId

def add_visiteur(insert):
    result = visiteurs.insert_one(insert)

def get_all(query):
    documents = list(visiteurs.find(query))
    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return documents

def trouver_visiteur(query: dict, page, limit):
    if len(query) != 0:
        visiteurs_list = list(visiteurs.find(query).skip((page - 1) * limit).limit(limit))
        for v in visiteurs_list:
            v["_id"] = str(v["_id"])

        return visiteurs_list
    else:
        return get_visiteurs(page, limit)


def get_visiteurs(page: int, limit: int):
    users = list(visiteurs.find({}, {"_id": 1, "nom": 1, "prenom": 1, "date_naissance": 1, "ville": 1, "departement_visite": 1}).skip((page - 1) * limit).limit(limit))
    total = visiteurs.count_documents({})
    for user in users:
        user["_id"] = str(user["_id"])

    return {"visiteurs": users, "total": total}


def get_infos(visiteur_id):
    infos = visiteurs.find_one({"_id": ObjectId(visiteur_id)})

    if infos:
        infos["_id"] = str(infos["_id"])

    return infos

def update_visiteur(visiteur_id: ObjectId, update: dict):
    visiteurs.update_one({"_id": visiteur_id}, {"$set": update})


def get_visiteurs_avec_filtre(query):
    return list(visiteurs.find(query, {"_id": 0}))

def reset_visiteurs():
    visiteurs.delete_many({})

def simu_utilisateurs():
    data = [
        {
            "prenom": "Lucas", "nom": "Martin", "mail": "lucas.martin@gmail.com",
            "date_naissance": "2006-03-15", "bac": "Bac Général",
            "specialite_1": "Mathématiques", "specialite_2": "Numérique et Sciences Informatiques",
            "filiere": None, "reorientation": False, "departement_visite": "INFO",
            "ville": "Lyon", "etablissement": "Lycée Saint-Exupéry",
            "immersion": True, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Camille", "nom": "Dupont", "mail": "camille.dupont@outlook.fr",
            "date_naissance": "2005-11-22", "bac": "Bac Technologique",
            "specialite_1": "", "specialite_2": "",
            "filiere": "STMG", "reorientation": False, "departement_visite": "GACO",
            "ville": "Paris", "etablissement": "Lycée Victor Hugo",
            "immersion": False, "evenement": "Salon de l'Étudiant",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Noah", "nom": "Bernard", "mail": "noah.bernard@yahoo.fr",
            "date_naissance": "2004-07-08", "bac": "Bac Professionnel",
            "specialite_1": "", "specialite_2": "",
            "filiere": None, "reorientation": True, "departement_visite": "INFOCOM",
            "ville": "Marseille", "etablissement": "Lycée Technique de Marseille",
            "immersion": False, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": "Actuellement en BTS, souhaite se réorienter"
        },
        {
            "prenom": "Léa", "nom": "Moreau", "mail": "lea.moreau@gmail.com",
            "date_naissance": "2006-01-30", "bac": "Bac Général",
            "specialite_1": "Physique-Chimie", "specialite_2": "Mathématiques",
            "filiere": None, "reorientation": False, "departement_visite": "INFO",
            "ville": "Bordeaux", "etablissement": "Lycée Montaigne",
            "immersion": True, "evenement": "Forum des Métiers",
            "situation_particuliere": True, "autre": "Dyslexie — aménagement souhaité"
        },
        {
            "prenom": "Théo", "nom": "Laurent", "mail": "theo.laurent@free.fr",
            "date_naissance": "2005-09-14", "bac": "Bac Technologique",
            "specialite_1": "", "specialite_2": "",
            "filiere": "STI2D", "reorientation": False, "departement_visite": "INFO",
            "ville": "Nantes", "etablissement": "Lycée Jules Verne",
            "immersion": True, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Inès", "nom": "Petit", "mail": "ines.petit@hotmail.fr",
            "date_naissance": "2006-05-19", "bac": "Bac Général",
            "specialite_1": "Sciences économiques et sociales",
            "specialite_2": "Histoire-Géographie, Géopolitique et Sciences Politiques",
            "filiere": None, "reorientation": False, "departement_visite": "GACO",
            "ville": "Toulouse", "etablissement": "Lycée Pierre de Fermat",
            "immersion": False, "evenement": "Salon de l'Étudiant",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Axel", "nom": "Roux", "mail": "axel.roux@gmail.com",
            "date_naissance": "2003-12-03", "bac": "Bac International",
            "specialite_1": "", "specialite_2": "",
            "filiere": None, "reorientation": True, "departement_visite": "INFO",
            "ville": "Strasbourg", "etablissement": "Lycée International de Strasbourg",
            "immersion": False, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": "Vient d'Allemagne, parle couramment anglais et allemand"
        },
        {
            "prenom": "Manon", "nom": "Simon", "mail": "manon.simon@laposte.net",
            "date_naissance": "2006-08-25", "bac": "Bac Général",
            "specialite_1": "Sciences de la Vie et de la Terre", "specialite_2": "Physique-Chimie",
            "filiere": None, "reorientation": False, "departement_visite": "QLIO",
            "ville": "Lille", "etablissement": "Lycée Pasteur",
            "immersion": True, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Hugo", "nom": "Michel", "mail": "hugo.michel@gmail.com",
            "date_naissance": "2005-04-11", "bac": "Bac Technologique",
            "specialite_1": "", "specialite_2": "",
            "filiere": "ST2S", "reorientation": False, "departement_visite": "INFOCOM",
            "ville": "Rennes", "etablissement": "Lycée Bréquigny",
            "immersion": False, "evenement": "Forum des Métiers",
            "situation_particuliere": True, "autre": "Mobilité réduite"
        },
        {
            "prenom": "Chloé", "nom": "Leroy", "mail": "chloe.leroy@sfr.fr",
            "date_naissance": "2006-02-07", "bac": "Bac Général",
            "specialite_1": "Arts", "specialite_2": "Humanités, Littérature et Philosophie",
            "filiere": None, "reorientation": False, "departement_visite": "INFOCOM",
            "ville": "Nice", "etablissement": "Lycée Masséna",
            "immersion": False, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Tom", "nom": "Garcia", "mail": "tom.garcia@gmail.com",
            "date_naissance": "2004-06-18", "bac": "Bac Professionnel",
            "specialite_1": "", "specialite_2": "",
            "filiere": None, "reorientation": True, "departement_visite": "QLIO",
            "ville": "Montpellier", "etablissement": "Lycée Jean Mermoz",
            "immersion": True, "evenement": "Salon de l'Étudiant",
            "situation_particuliere": False, "autre": "Souhaite valider ses acquis professionnels"
        },
        {
            "prenom": "Jade", "nom": "Martinez", "mail": "jade.martinez@gmail.com",
            "date_naissance": "2006-10-05", "bac": "Bac Général",
            "specialite_1": "Numérique et Sciences Informatiques", "specialite_2": "Mathématiques",
            "filiere": None, "reorientation": False, "departement_visite": "INFO",
            "ville": "Grenoble", "etablissement": "Lycée Stendhal",
            "immersion": True, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Enzo", "nom": "Lefebvre", "mail": "enzo.lefebvre@orange.fr",
            "date_naissance": "2005-07-29", "bac": "Bac Technologique",
            "specialite_1": "", "specialite_2": "",
            "filiere": "STD2A", "reorientation": False, "departement_visite": "INFOCOM",
            "ville": "Dijon", "etablissement": "Lycée Le Castel",
            "immersion": False, "evenement": "Forum des Métiers",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Alice", "nom": "Dubois", "mail": "alice.dubois@gmail.com",
            "date_naissance": "2006-03-22", "bac": "Bac Général",
            "specialite_1": "Langues, Littératures et Cultures Étrangères",
            "specialite_2": "Sciences économiques et sociales",
            "filiere": None, "reorientation": False, "departement_visite": "GACO",
            "ville": "Angers", "etablissement": "Lycée David d'Angers",
            "immersion": False, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Raphaël", "nom": "Fontaine", "mail": "raphael.fontaine@proton.me",
            "date_naissance": "2003-09-01", "bac": "Bac International",
            "specialite_1": "", "specialite_2": "",
            "filiere": None, "reorientation": True, "departement_visite": "INFO",
            "ville": "Clermont-Ferrand", "etablissement": "Lycée Blaise Pascal",
            "immersion": True, "evenement": "Salon de l'Étudiant",
            "situation_particuliere": False, "autre": "Vient d'une prépa MPSI"
        },
        {
            "prenom": "Zoé", "nom": "Girard", "mail": "zoe.girard@hotmail.com",
            "date_naissance": "2006-12-14", "bac": "Bac Général",
            "specialite_1": "Sciences et Techniques Sanitaires et Sociales",
            "specialite_2": "Sciences de la Vie et de la Terre",
            "filiere": None, "reorientation": False, "departement_visite": "QLIO",
            "ville": "Tours", "etablissement": "Lycée Paul-Louis Courier",
            "immersion": False, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": True, "autre": "TDAH diagnostiqué"
        },
        {
            "prenom": "Nathan", "nom": "Bonnet", "mail": "nathan.bonnet@gmail.com",
            "date_naissance": "2005-05-03", "bac": "Bac Technologique",
            "specialite_1": "", "specialite_2": "",
            "filiere": "STL", "reorientation": False, "departement_visite": "INFO",
            "ville": "Rouen", "etablissement": "Lycée Blaise Pascal",
            "immersion": True, "evenement": "Forum des Métiers",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Eva", "nom": "Chevalier", "mail": "eva.chevalier@free.fr",
            "date_naissance": "2006-08-17", "bac": "Bac Général",
            "specialite_1": "Mathématiques", "specialite_2": "Sciences économiques et sociales",
            "filiere": None, "reorientation": False, "departement_visite": "GACO",
            "ville": "Reims", "etablissement": "Lycée Roosevelt",
            "immersion": False, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
        {
            "prenom": "Liam", "nom": "Morel", "mail": "liam.morel@gmail.com",
            "date_naissance": "2004-11-09", "bac": "Bac Professionnel",
            "specialite_1": "", "specialite_2": "",
            "filiere": None, "reorientation": True, "departement_visite": "QLIO",
            "ville": "Le Mans", "etablissement": "Lycée Technique du Mans",
            "immersion": True, "evenement": "Salon de l'Étudiant",
            "situation_particuliere": False, "autre": "Expérience en logistique de 2 ans"
        },
        {
            "prenom": "Emma", "nom": "Perrin", "mail": "emma.perrin@laposte.net",
            "date_naissance": "2006-04-26", "bac": "Bac Technologique",
            "specialite_1": "", "specialite_2": "",
            "filiere": "STHR", "reorientation": False, "departement_visite": "GACO",
            "ville": "Caen", "etablissement": "Lycée Malherbe",
            "immersion": False, "evenement": "Journée Portes Ouvertes",
            "situation_particuliere": False, "autre": None
        },
    ]

    visiteurs.insert_many(data)