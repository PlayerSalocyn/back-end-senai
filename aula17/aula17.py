from fastapi import FastAPI
from pydantic import BaseModel
#criar a instância da api
app=FastAPI(title="Rotas fake API")
#endpoint simples para teste da api
@app.get("/")
async def teste_api():
    return{"messagem":"Teste get api"}
#rodar api #pasta do arquivo da api
#python -m uvicorn nome_arquivo:app --reload
#produtos fake para teste
produtos={
    1:{"nome":"caneta","price":2.55,"quantidade":100},
    2:{"nome":"lapis","price":1.55,"quantidade":100},
    3:{"nome":"borracha","price":0.55,"quantidade":100},
    }
#endpoint produtos
@app.get("/produtos")
async def get_produto():
    return produtos
#endpoint produtos pelo id path parameter
@app.get("/get-produtos/{id_produto}")
async def produtos_id(id_produto:int):
    return produtos[id_produto]
#endpoint produto por nome query parameter
@app.get("/get-produto-nome")
async def get_produto_nome(nome:str):
    for i in produtos:#loop para rodar os dados
        if produtos[i]["nome"] ==nome:#retorna nome se for igual
            return produtos[i]#retorna o produto pelo index
    return {"DADOS":"Produto não encontrado"}
#método post put delete
#manipulação de dados com o pydantic
class Item(BaseModel):
    #objeto produto nome, preço e quantidade
    nome:str
    price:float
    quantidade:int
#endpoint post criar um item em produtos
@app.post("/items/")
async def criar_item(item:Item):#instânciar o BaseModel Item
    return {"item":item}
#endpoint para atualizar um item PUT
@app.put("/items-update/{item_id}")#atualizar item pelo id
async def update_item(item_id:int,item:Item):#pesquisar pelo id e instâciar o BaseModel
    return {"item_id":item_id,"update_item":item}
#endpoint para deletar item delete
@app.delete("/items-deletar/{item_id}")#rota para deletar item
async def deletar_item(item_id:int):
    return {"messagem":f"Item {item_id} deletado. "}