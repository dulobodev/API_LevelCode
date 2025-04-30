from pydantic import BaseModel


class ModuleBase(BaseModel):
    nome: str

    class Config:
        from_attributes = True


class ModuleCreate(ModuleBase):
    pass


class ModuleResponse(ModuleBase):
    id: int
