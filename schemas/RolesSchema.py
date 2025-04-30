from pydantic import BaseModel
from typing import List

class PermissionCreate(BaseModel):
    nome: str
    
    class Config:
        from_attributes = True
        schema_extra = {
            "example": {
                "nome": "nome_da_permissao"
            }
        }


class RolesCreate(BaseModel):
    id: int = None
    nome: str = 'user'
    permissions: List[PermissionCreate] = []

    class Config:
        from_attributes = True
