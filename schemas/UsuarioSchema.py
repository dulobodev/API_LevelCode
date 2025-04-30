from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    desafios: int = 0
    nivel: int = 0
    xp_total: int = 0
    roles_id: int 
    ranking_id : int = 1

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    nome : str
    senha : str
