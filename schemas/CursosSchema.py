from pydantic import BaseModel
from typing import List


class ModuleCreate(BaseModel):
    nome: str

    class Config:
        from_attributes = True

class CourseBase(BaseModel):
    titulo: str
    descricao: str
    dificuldade: str
    xp_total: int

    class Config:
        from_attributes = True


class CourseCreate(CourseBase):
    modulos: List[ModuleCreate]


class CourseResponse(CourseBase):
    id: int
    modulos: List[ModuleCreate]

class UsuarioCursoCreate(BaseModel):
    user_id : int
    curso_id : int