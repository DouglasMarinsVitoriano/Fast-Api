import datetime
from typing import Optional
import ormar

from config import database, metadata
from models.cargos import Papel

class Salario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "salarios"
    
    id: int = ormar.Integer(primary_key=True)
    valor: float = ormar.Float(minimum=0)
    horario: datetime = ormar.DateTime(timezone=False)
    papel: Optional[Papel] = ormar.ForeignKey(
        Papel,
        skip_reverse=True
    )