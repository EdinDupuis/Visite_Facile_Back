from flask import Blueprint, jsonify, request, Response
from services import visiteurs_service
from services.visiteur import Visiteur

visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')


@visiteurs_controller.route('/visiteurs', methods=['POST'])
def add_teacher() -> tuple[Response, int]:
    data = request.get_json()
    visiteur = Visiteur(data['id'], data['name'], [])
    visiteurs_service.add_teacher(visiteur)
    return jsonify(), 201
