from flask import Blueprint, jsonify, request, Response
from VisiteFacile.services import visiteurs_service
from VisiteFacile.services.visiteur import Visiteur

teachers_controller = Blueprint('visiteurs', __name__, url_prefix='/visiteurs')