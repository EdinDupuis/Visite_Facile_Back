from flask import Blueprint, jsonify, request, Response

import services.visiteurs_service
from dtos.VisiteurDTO import VisiteurDTO
from services import visiteurs_service
from utils.connect import bd, visiteurs

visiteurs_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')


@visiteurs_controller.route('/', methods=['POST'])
def add_visiteur() -> tuple[Response, int]:
    data = request.get_json()

    visiteur = VisiteurDTO(
        prenom=data.get('prenom'),
        nom=data.get('nom'),
        mail=data.get('mail'),
        date_naissance=data.get('data_naissance'),
        bac = data.get('bac'),
        specialite_1=data.get('specialite_1'),
        specialite_2=data.get('specialite_2'),
        reorientation=data.get('reorientation'),
        departement_visite=data.get('departement_visite'),
        ville=data.get('ville'),
        etablissement=data.get('etablissement'),
        immersion=data.get('immersion'),
        evenement=data.get('evenement'),
        autre=data.get('autre')
    )

    result = services.visiteurs_service.add_visiteur(visiteur)

    return jsonify(result), 201
