from dotenv import dotenv_values
from flask import Blueprint, jsonify, request, Response


from VisiteFacile.dtos.ParametresDTO import UpdateParametresDTO
from VisiteFacile.services import visiteurs_service, parametres_service
from VisiteFacile.dtos.VisiteurDTO import *

visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')

@visiteurs_controller.route('/', methods=['POST'])
def add_visiteur() -> tuple[Response, int]:
    data = request.get_json()
    visiteur = CreateVisiteurDTO.model_validate(
        data
    )
    result = visiteurs_service.add_visiteur(visiteur)
    return jsonify(result), 201


@visiteurs_controller.route('/filtre', methods=['GET'])
def get_visiteurs():
    query = {}

    nom = request.args.get('nom')
    prenom = request.args.get('prenom')
    date_naissance = request.args.get('date_naissance')
    bac = request.args.get('bac')
    specialite_1 = request.args.get('specialite_1')
    specialite_2 = request.args.get('specialite_2')
    reorientation = request.args.get('reorientation')
    departement_visite = request.args.get('departement_visite')
    ville = request.args.get('ville')
    etablissement = request.args.get('etablissement')
    immersion = request.args.get('immersion')
    evenement = request.args.get('evenement')
    situation_particuliere = request.args.get('situation_particuliere')

    limit: int = request.args.get("limit", 5, type=int)
    page: int = request.args.get("page", 1, type=int)

    if nom:
        query['nom'] = {'$regex': nom, '$options': 'i'}
    if prenom:
        query['prenom'] = {'$regex': prenom, '$options': 'i'}
    if etablissement:
        query['etablissement'] = {'$regex': etablissement, '$options': 'i'}
    if date_naissance:
        query['date_naissance'] = {'$regex': date_naissance, '$options': 'i'}
    if bac:
        query['bac'] = {'$regex': bac, '$options': 'i'}
    if specialite_1:
        query['specialite_1'] = {'$regex': specialite_1, '$options': 'i'}
    if specialite_2:
        query['specialite_2'] = {'$regex': specialite_2, '$options': 'i'}
    if departement_visite:
        query['departement_visite'] = {'$regex': departement_visite, '$options': 'i'}
    if ville:
        query['ville'] = {'$regex': ville, '$options': 'i'}
    if evenement:
        query['evenement'] = {'$regex': evenement, '$options': 'i'}

    if reorientation == 'true':
        query['reorientation'] = True
    if immersion == 'true':
        query['immersion'] = True
    if situation_particuliere == 'true':
        query['situation_particuliere'] = True

    resultat = visiteurs_service.trouver_visiteurs(query, page, limit)
    return jsonify(resultat), 200


@visiteurs_controller.route('/<string:visiteur_id>', methods=['DELETE'])
def delete_visiteur(visiteur_id: str) -> tuple[Response, int]:
    result = visiteurs_service.del_visiteur(visiteur_id)

    if result.deleted_count > 0:
        return jsonify({"message": "Visiteur supprimé"}), 200
    else:
        return jsonify({"message": "Visiteur non trouvé"}), 404


@visiteurs_controller.route('/<visiteur_id>', methods=['GET'])
def details_visiteurs(visiteur_id: str) -> tuple[Response, int]:
    info = visiteurs_service.get_infos(visiteur_id)
    if not info:
        return jsonify(), 404
    return jsonify(info), 200


@visiteurs_controller.route('/<id>', methods=['PUT'])
def update_visiteur(id: str) -> tuple[Response, int]:
    data = request.get_json()

    visiteur = UpdateVisiteurDTO.model_validate(
        data
    )

    result = visiteurs_service.update_visiteur(visiteur, id)
    if not result:
        return jsonify(), 404
    return '', 204


@visiteurs_controller.route('/login', methods=['GET'])
def login_admin() -> tuple[Response, int]:
    mdp = request.args.get('mdp', '', type=str)
    env_values = dotenv_values(".env")
    password = env_values["ADMIN_PASSWORD"]
    if mdp.__eq__(password):
        return jsonify({'ok': True}), 200
    return jsonify({'ok': False}), 401


@visiteurs_controller.route('stats/export', methods=['GET'])
def export_visiteurs() -> tuple[Response, int]:
    fichier = visiteurs_service.get_export(request.args)

    if fichier is None:
        return jsonify(), 404

    return Response(fichier, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=visiteurs.csv"}), 200


@visiteurs_controller.route('/parametres', methods=['PUT'])
def update_parametres() -> tuple[Response, int]:
    data = request.get_json()

    parametre = UpdateParametresDTO.model_validate(
        data
    )
    result = parametres_service.update_parametres(parametre)
    if not result:
        return jsonify(), 404
    return '', 204