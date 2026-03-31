from flask import Blueprint, jsonify, request, Response

from VisiteFacile.services import visiteurs_service
from VisiteFacile.dtos.VisiteurDTO import *

visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')


@visiteurs_controller.route('/', methods=['GET'])
def find_all() -> tuple[Response, int]:


    limit: int = request.args.get("limit", 20, type = int)
    page: int = request.args.get("page", 0, type = int)

    resultat = visiteurs_service.get_visiteurs(limit, page)
    return jsonify(resultat), 200


@visiteurs_controller.route('/', methods=['POST'])
def add_visiteur() -> tuple[Response, int]:
    data = request.get_json()
    visiteur = VisiteurDTO.model_validate_json(
        **data
    )
    result = visiteurs_service.add_visiteur(visiteur)
    return jsonify(result), 201


@visiteurs_controller.route('/', methods=['GET'])
def get_visiteurs():
    query = {}

    nom = request.args.get('nom')
    prenom = request.args.get('prenom')
    date_naissance = request.args.get('date_naissance')
    specialite_1 = request.args.get('specialité_1')
    specialite_2 = request.args.get('specialité_2')
    reorientation = request.args.get('réorientation')
    departement_visite = request.args.get('département_visité')
    ville = request.args.get('ville')
    etablissement = request.args.get('établissement')
    immersion = request.args.get('immersion')
    evenement = request.args.get('évènement')

    limit: int = request.args.get("limit", 20, type = int)
    page: int = request.args.get("page", 0, type = int)

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



@visiteurs_controller.route('/<visiteur_id>', methods=['GET'])
def details_visiteurs(visiteur_id: str) -> tuple[Response, int]:
    info = visiteurs_service.get_infos(visiteur_id)
    if not info:
        return jsonify(), 404
    return jsonify(info), 200

@visiteurs_controller.route('details/<id>', methods=['PUT'])
def update_visiteur(id: str) -> tuple[Response, int]:
    data = request.get_json()

    visiteur = UpdateVisiteurDTO(
        prenom=data.get('prenom'),
        nom=data.get('nom'),
        mail=data.get('mail'),
        date_naissance=data.get('date_naissance'),
        bac=data.get('bac'),
        specialite_1=data.get('specialite_1'),
        specialite_2=data.get('specialite_2'),
        filiere=data.get('filiere'),
        reorientation=data.get('reorientation'),
        departement_visite=data.get('departement_visite'),
        ville=data.get('ville'),
        etablissement=data.get('etablissement'),
        immersion=data.get('immersion'),
        autre=data.get('autre')
    )

    result = visiteurs_service.update_visiteur(visiteur, id)

    return jsonify(result), 204

