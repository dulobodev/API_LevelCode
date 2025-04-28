from pydantic import BaseModel
from datetime import datetime

class UserConquestBase(BaseModel):
    datetime: datetime
    user_id: int
    aula_id: int

    class Config:
        orm_mode = True

class ConquestBase(BaseModel):
    nome: str
    criterios: str

    class Config:
        orm_mode = True



class ConquestCreate(ConquestBase):
    pass


class ConquestResponse(ConquestBase):
    id: int
