from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserBase(BaseModel):
    nome: str
    email: EmailStr
    senha_hash: str
    challenges: int = 0
    nivel: int = 0
    xp_total: int = 0

    class Config:
        orm_mode = True



class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
