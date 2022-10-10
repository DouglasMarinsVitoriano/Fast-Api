from fastapi import APIRouter
import ormar
from controllers.utils.delete_controller import delete_controller
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.patch_controller import patch_controller
from controllers.utils.post_controller import post_controller

from models.cargos import Cargos
from models.requests.salario_update import SalarioUpdate

router = APIRouter()

@router.post("/")
@post_controller
async def add_item(entidade: Cargos):
    pass

@router.get("/")
@get_all_controller(Cargos)
async def list_item():
    pass

@router.get("/{id}")
@get_controller(Cargos)
async def get_Cargos(id: int):    
    pass

@router.patch("/{id}")
@patch_controller(Cargos)
async def patch_Cargos(propriedades_atualizacao: Cargos, id: int):
    pass

@router.delete("/{id}")
@delete_controller(Cargos)
async def delete_Cargos(id: int):
    pass