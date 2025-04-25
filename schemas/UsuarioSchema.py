from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserBase(BaseModel):
    nome: str
    email: EmailStr
    senha_hash: str
    challenges: int
    nivel: int
    xp_total: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
