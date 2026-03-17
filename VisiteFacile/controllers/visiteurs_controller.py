from flask import Blueprint, jsonify, request, Response

import services.visiteurs_service
from services import visiteurs_service
from utils.connect import bd, visiteurs
from datetime import date


visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')

@visiteurs_controller.route('/', methods=['GET'])
def find_all() -> tuple[Response, int]:
    _id: int = request.args.get('_id', '', type=int)
    nom: str = request.args.get('nom', '', type=str)
    prénom: str = request.args.get('prénom', '', type=str)
    date_naissance: str = request.args.get('date_naissance', '', type=str)
    ville: str = request.args.get('ville', '', type=str)
    département_visité: str = request.args.get('département_visité', '', type=str)
    limit: int = request.args.get('limit', 20, type=int)
    page: int = request.args.get('page', 1, type=int)
    resultat = visiteurs_service.get_visiteurs()
    return jsonify(resultat), 200

@visiteurs_controller.route('/', methods=['POST'])
def add_visiteur() -> tuple[Response, int]:
    existing_fields = {"prénom", "nom", "mail", "date_naissance", "bac_préparé", "specialité_1","specialité_2", "réorientation",
                       "département_visité", "ville", "établissement", "immersion", "évènement", "autre"}
    data = request.get_json()

    visiteur = {}

    for key, value in data.items():
        if key in existing_fields:
            visiteur[key] = value

    services.visiteurs_service.add_visiteur(visiteur)

    return jsonify(), 201
