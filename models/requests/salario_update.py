from typing import List, Optional
from pydantic import BaseModel

class SalarioUpdate(BaseModel):
    nome: Optional[str] = None
    cnpj: Optional[str] = None