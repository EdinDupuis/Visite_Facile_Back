from flask import Blueprint, jsonify, request, Response
import services
from services import visiteurs_service


visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')

@visiteurs_controller.route('/<string:visiteur_nom>', methods=['GET'])
def access_by_name(visiteur_nom: str) -> tuple[Response, int]:

    resultat = visiteurs_service.trouver_visiteur_par_nom(visiteur_nom)

    return jsonify(resultat), 200

@visiteurs_controller.route('/', methods=['POST'])
def add_visiteur() -> tuple[Response, int]:
    existing_fields = {"prenom", "nom", "mail", "data_naissance","specialité_1","specialité_2", "réorientation",
                       "département_visité", "ville", "établissement", "immersion", "évènement", "autre"}
    data = request.get_json()

    visiteur = {}

    for key, value in data.items():
        if key in existing_fields:
            visiteur[key] = value

    services.visiteurs_service.add_visiteur(visiteur)

    return jsonify(), 201

