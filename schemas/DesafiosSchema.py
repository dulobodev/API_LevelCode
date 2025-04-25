from pydantic import BaseModel


class ChallengeBase(BaseModel):
    nome: str
    desafio: str
    requisitos: str
    resultado: str
    xp: int

    class Config:
        orm_mode = True


class ChallengeCreate(ChallengeBase):
    pass


class ChallengeResponse(ChallengeBase):
    id: int
