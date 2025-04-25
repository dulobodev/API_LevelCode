from pydantic import BaseModel


class ProgressBase(BaseModel):
    status: str
    data_conclusao: str
    user_id: int
    module_id: int

    class Config:
        orm_mode = True


class ProgressCreate(ProgressBase):
    pass


class ProgressResponse(ProgressBase):
    pass
