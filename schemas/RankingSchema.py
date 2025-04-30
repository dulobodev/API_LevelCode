from pydantic import BaseModel
from datetime import datetime


class RankingBase(BaseModel):
    nome: str
    privilegios: str
    requisitos: str


    class Config:
        from_attributes = True


class RankingCreate(RankingBase):
    pass


class RankingResponse(RankingBase):
    id: int
