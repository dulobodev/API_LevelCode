from pydantic import BaseModel


class ChallengeBase(BaseModel):
    nome: str
    descricao: str
    requisitos: str
    resultado: str
    xp: int

    class Config:
        from_attributes = True


class ChallengeCreate(ChallengeBase):
    pass


class ChallengeResponse(ChallengeBase):
    id: int
