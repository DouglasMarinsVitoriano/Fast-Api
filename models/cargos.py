# Modelos para validarmos os cargos


import ormar
import re
from pydantic import validator
from sqlalchemy.sql.expression import table
from config import database, metadata

class Cargos(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "cargos"

    id: int = ormar.Integer(primary_key=True)
    cargos: str = ormar.String(max_length=100)
    tempo_de_empresa: float = ormar.Float(max_length=10)
    

    @validator('sigla')
    def valida_formatacao_sigla(cls, v):
        if not re.compile('^[A-Z]{4}[0-9]{1,2}$').match(v):
            raise ValueError('A sigla do papel é inválida!')
        return v