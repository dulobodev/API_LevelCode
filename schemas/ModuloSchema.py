from pydantic import BaseModel


class ModuleBase(BaseModel):
    nome: str
    curso_id: int

    class Config:
        orm_mode = True


class ModuleCreate(ModuleBase):
    pass


class ModuleResponse(ModuleBase):
    id: int
