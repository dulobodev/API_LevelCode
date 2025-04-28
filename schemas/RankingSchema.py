from pydantic import BaseModel
from datetime import datetime


class RankingBase(BaseModel):
    nome: str
    privilegios: str
    requisitos: str
    created_date: datetime
    user_id: int

    class Config:
        orm_mode = True


class RankingCreate(RankingBase):
    pass


class RankingResponse(RankingBase):
    id: int
