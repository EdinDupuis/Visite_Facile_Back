from flask import Blueprint, jsonify, request, Response
from services import visiteurs_service

visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')
def access_by_id(visiteur_nom: str) -> tuple[Response, int]:
    data = request.get_json()

    resultat = visiteurs_service.trouver_visiteur_par_nom(visiteur_nom, data)

    return jsonify(resultat), 200