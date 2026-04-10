from typing import Optional

from pydantic import BaseModel, ConfigDict


class UpdateParametresDTO(BaseModel):
    mdp: Optional[str] = None
    #D'autres paramètres peut-être ?

class CheckMdpDTO(BaseModel):
    ancienMdp: str

class LoginDTO(BaseModel):
    motDePasse: str