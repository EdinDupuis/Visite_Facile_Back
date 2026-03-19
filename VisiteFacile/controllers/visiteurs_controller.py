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

    limit: int = request.args.get('limit', 20, type=int)
    page: int = request.args.get('page', 1, type=int)

    if nom:
        query['nom'] = {'$regex': nom, '$options': 'i'}
    if prenom:
        query['prenom'] = {'$regex': prenom, '$options': 'i'}
    if etablissement:
        query['établissement'] = {'$regex': etablissement, '$options': 'i'}
    if date_naissance:
        query['date_naissance'] = date_naissance
    if specialite_1:
        query['specialité_1'] = {'$regex': specialite_1, '$options': 'i'}
    if specialite_2:
        query['specialité_2'] = {'$regex': specialite_2, '$options': 'i'}
    if reorientation:
        query['réorientation'] = {'$regex': reorientation, '$options': 'i'}
    if departement_visite:
        query['département_visité'] = {'$regex': departement_visite, '$options': 'i'}
    if ville:
        query['ville'] = {'$regex': ville, '$options': 'i'}
    if immersion:
        query['immersion'] = {'$regex': immersion, '$options': 'i'}
    if evenement:
        query['évènement'] = {'$regex': evenement, '$options': 'i'}

    resultat = visiteurs_service.trouver_visiteurs(query, limit, page)
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

