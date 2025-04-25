from pydantic import BaseModel
from datetime import datetime


class UserConquestBase(BaseModel):
    usuario_id: int
    conquest_id: int
    created_date: datetime

    class Config:
        orm_mode = True


class UserConquestCreate(UserConquestBase):
    pass


class UserConquestResponse(UserConquestBase):
    id: int
