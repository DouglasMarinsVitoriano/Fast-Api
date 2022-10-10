from tests.utils.cargos import create_cargos_valido, create_cargos_invalido
from models.cargos import Cargos
import pytest

def test_cria_cargos_valido() -> None:
    atributos = create_cargos_valido()
    cargos = cargos(**atributos)

def test_cria_cargos_com_sigla_invalida() -> None:
    with pytest.raises(ValueError, match='A sigla do cargos é inválida!'):
        atributos = create_cargos_invalido(['sigla'])
        cargos = cargos(**atributos)