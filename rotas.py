from fastapi import APIRouter

from controllers import salario_controller as papeis
from controllers import cargos_controller as cotacoes
from controllers import usuario_controller as usuario

router = APIRouter()

router.include_router(papeis.router, prefix='/papeis', tags=['Papeis'])

router.include_router(cotacoes.router, prefix='/cotacoes', tags=['Cotações'])

router.include_router(usuario.router, prefix='/usuarios', tags=['Usuario'])