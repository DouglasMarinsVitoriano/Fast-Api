from fastapi.testclient import TestClient
from models.cargos import Cargos
from tests.utils.cargos import create_cargos_invalido, create_cargos_valido
import asyncio
import pytest
import ormar

def test_lista_todos_os_papeis(client: TestClient) -> None:
    atributos = create_cargos_valido()
    Cargos = Cargos(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Cargos.save())
    
    response = client.get("/papeis/")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

def test_cria_cargos(client: TestClient) -> None:
    body = create_cargos_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]

def test_cria_cargos_com_sigla_invalida(client: TestClient) -> None:
    body = create_cargos_invalido(['sigla'])
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 422

def test_obtem_um_cargos_por_id(client: TestClient) -> None:
    atributos = create_cargos_valido()
    Cargos =Cargos(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Cargos.save())

    response = client.get(f"/papeis/{Cargos.id}")
    content = response.json()

    assert response.status_code == 200
    assert content["sigla"] ==Cargos.sigla

def test_obtem_cargos_inexistente_por_id(client: TestClient) -> None:
    response = client.get(f"/papeis/1")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"

def test_update_cargos_existente(client: TestClient) -> None:
    atributos = create_cargos_valido()
    Cargos =Cargos(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Cargos.save())

    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}

    response = client.patch(f"/papeis/{Cargos.id}", json=atributos_para_atualizar)
    content = response.json()

    Cargos_atualizado = loop.run_until_complete(Cargos.objects.get(id=Cargos.id))

    assert response.status_code == 200
    assert content["nome"] == novo_nome
    assert Cargos_atualizado.nome == novo_nome


def test_update_cargos_inexistente(client: TestClient) -> None:
    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}

    response = client.patch(f"/papeis/1", json=atributos_para_atualizar)
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"


def test_delete_cargos_existente(client: TestClient) -> None:
    atributos = create_cargos_valido()
    Cargos =Cargos(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Cargos.save())

    response = client.delete(f"/papeis/{Cargos.id}")

    with pytest.raises(ormar.exceptions.NoMatch): 
        loop.run_until_complete(Cargos.objects.get(id=Cargos.id))

    assert response.status_code == 200


def test_delete_cargos_inexistente(client: TestClient) -> None:
    response = client.delete(f"/papeis/1")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"