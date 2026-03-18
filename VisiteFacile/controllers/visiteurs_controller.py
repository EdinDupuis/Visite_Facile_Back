from flask import Blueprint, jsonify, request, Response
import services
from services import visiteurs_service
from utils.connect import bd, visiteurs


visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')

@visiteurs_controller.route('/', methods=['GET'])
def get_visiteurs():
    query = {}

    nom = request.args.get('nom')
    prenom = request.args.get('prenom')
    date_naissance = request.args.get('date_naissance')
    specialite_1 = request.args.get('specialité_1')
    specialite_2 = request.args.get('specialité_2')
    reorientation =request.args.get('réorientation')
    departement_visite = request.args.get('département_visité')
    ville = request.args.get('ville')
    etablissement = request.args.get('établissement')
    immersion = request.args.get('immersion')
    evenement = request.args.get('évènement')

    if nom:
        query['nom'] = nom
    if prenom:
        query['prenom'] = prenom
    if etablissement:
        query['établissement'] = etablissement
    if date_naissance:
        query['date_naissance'] = date_naissance
    if specialite_1:
        query['specialité_1'] = specialite_1
    if specialite_2:
        query['specialité_2'] = specialite_2
    if reorientation:
        query['réorientation'] = reorientation
    if departement_visite:
        query['département_visité'] = departement_visite
    if ville:
        query['ville'] = ville
    if immersion:
        query['immersion'] = immersion
    if evenement:
        query['évènement'] = evenement

    resultat = visiteurs_service.trouver_visiteurs(query)
    return jsonify(resultat), 200


@visiteurs_controller.route('/', methods=['POST'])
def add_visiteur() -> tuple[Response, int]:
    existing_fields = {"prenom", "nom", "mail", "date_naissance","specialité_1","specialité_2", "réorientation",
                       "département_visité", "ville", "établissement", "immersion", "évènement", "autre"}
    data = request.get_json()

    visiteur = {}

    for key, value in data.items():
        if key in existing_fields:
            visiteur[key] = value

    services.visiteurs_service.add_visiteur(visiteur)

    return jsonify(), 201

