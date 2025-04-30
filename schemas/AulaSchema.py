from pydantic import BaseModel


class ClassBase(BaseModel):
    titulo: str
    conteudo: str
    modulo_id: int
    xp: int

    class Config:
        from_attributes = True


class ClassCreate(ClassBase):
    pass


class ClassResponse(ClassBase):
    id: int
