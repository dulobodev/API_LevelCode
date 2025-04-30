from pydantic import BaseModel


class ProgressBase(BaseModel):
    status: str
    usuario_id: int
    aula_id : int

    class Config:
        from_attributes = True


class ProgressCreate(ProgressBase):
    pass


class ProgressResponse(ProgressBase):
    pass
