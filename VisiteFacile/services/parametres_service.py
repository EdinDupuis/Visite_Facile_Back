from VisiteFacile.dtos.ParametresDTO import UpdateParametresDTO
from dotenv import set_key


def update_parametres(dto: UpdateParametresDTO):
    mdp = dto.mdp
    return set_key(".env", "ADMIN_PASSWORD", mdp)
