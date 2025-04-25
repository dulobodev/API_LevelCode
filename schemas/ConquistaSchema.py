from pydantic import BaseModel


class ConquestBase(BaseModel):
    nome: str
    criterios: str
    user_id: int
    aula_id: int

    class Config:
        orm_mode = True


class ConquestCreate(ConquestBase):
    pass


class ConquestResponse(ConquestBase):
    id: int
