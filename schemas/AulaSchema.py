from pydantic import BaseModel


class ClassBase(BaseModel):
    titulo: str
    conteudo: str
    modulo_id: int
    xp: int

    class Config:
        orm_mode = True


class ClassCreate(ClassBase):
    pass


class ClassResponse(ClassBase):
    id: int
