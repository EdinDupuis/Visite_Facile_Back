from typing import Optional

from pydantic import BaseModel, ConfigDict


class UpdateParametresDTO(BaseModel):
    mdp: Optional[str] = None
    #D'autres paramètres peut-être ?
