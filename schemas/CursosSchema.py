from pydantic import BaseModel
from typing import List, Optional


class ModuleCreate(BaseModel):
    nome: str

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    titulo: str
    descricao: str
    dificuldade: str
    xp_total: int

    class Config:
        orm_mode = True


class CourseCreate(CourseBase):
    modulos: List[ModuleCreate]


class CourseResponse(CourseBase):
    id: int
    modulos: List[ModuleCreate]