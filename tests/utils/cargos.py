def create_cargos_valido():
    return {
        "id": 0,
        "nome": "string",
        "sigla": "PETR4",
        "cnpj": "string",
    }

def create_cargos_invalido(campos_invalidos=['sigla']):
    cargos_invalido = {
        "id": 0,
        "nome": "string",
        "sigla": "PETR4",
        "cnpj": "string",
    }

    if 'sigla' in campos_invalidos:
        cargos_invalido['sigla'] = 'AAAAAAAA'
    
    return cargos_invalido