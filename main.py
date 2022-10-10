"""
Para rodas a API uvicorn main:app --reload
Get = para ler dados
Post = criar dados
put = para atualizar dados
delete = deletar dados
"""

from fastapi import FastAPI

from rotas import router

app = FastAPI()

@app.get("/")
def get_root():
    return {"mensagem": "api de papeis"}

app.include_router(router, prefix="")