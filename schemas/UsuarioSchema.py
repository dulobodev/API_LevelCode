from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserBase(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    desafios: int = 0
    nivel: int = 0
    xp_total: int = 0
    roles_id: int 

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
