from flask import Blueprint, jsonify, request, Response

import services.visiteurs_service
from services import visiteurs_service
from utils.connect import bd, visiteurs

visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')


@visiteurs_controller.route('/', methods=['POST'])
def add_visiteur() -> tuple[Response, int]:
    existing_fields = {"prenom", "nom", "mail", "data_naissance,specialité_1,specialité_2", "réorientation",
                       "département_visité", "ville", "établissement", "immersion", "évènement", "autre"}
    data = request.get_json()

    visiteur = {}

    for key, value in data.items():
        if key in existing_fields:
            visiteur[key] = value

    services.visiteurs_service.add_visiteur(visiteur)

    return jsonify(), 201
