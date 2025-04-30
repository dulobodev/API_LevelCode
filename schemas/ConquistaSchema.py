from pydantic import BaseModel

class UserConquestBase(BaseModel):
    usuario_id: int
    conquista_id: int

    class Config:
        from_attributes = True

class ConquestBase(BaseModel):
    nome: str
    criterios: str

    class Config:
        from_attributes = True



class ConquestCreate(ConquestBase):
    pass


class ConquestResponse(ConquestBase):
    id: int
