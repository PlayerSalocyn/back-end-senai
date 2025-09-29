from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
app = FastAPI(title="API itens com sqlite")

BANCO = "itens.db"

def criar_tabela():
    conn=sqlite3.connect(BANCO)
    cur= conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                price REAL NOT NULL,
                quantidade INTEGER NOT NULL)""")
    conn.commit()
    conn.close()
# criar_tabela()
'''
conn = sqlite3.connect(BANCO)
cur = conn.cursor()
cur.execute("""INSERT INTO itens (
            nome, price, quantidade) VALUES ('caneta', 1.75, 5)""")
conn.commit
'''

class Item(BaseModel):
    nome: str
    price: float
    quantidade: int
#endpoint para listar todos os itens (GET)
@app.get("/")
async def listar_itens():
    conn = sqlite3.connect(BANCO)
    cur= conn.cursor()
    cur.execute("SELECT * FROM itens")
    linhas = cur.fetchall()
    return {"itens": linhas}

@app.get("/itens/{item_id}")
async def get_item(item_id:id):
    conn = sqlite3.connect(BANCO)
    cur= conn.cursor()
    cur.execute("SELECT * FROM itens WHERE id=?",
                (item_id,))
    item = cur.fetchall()
    if item: 
        return{"item": item}
    return {"ERRO":"Item não encontrado."}
@app.post("/itens-criar")
async def criar_item(item: Item):
    conn = sqlite3.connect(BANCO)
    cur= conn.cursor()
    cur.execute("""INSERT INTO itens (
    nome,price,quantidade) VALUES (?,?,?)""", (item.nome,item.price,item.quantidade))
    conn.commit()
    item_id=cur.lastrowid
    return {'id': item_id, "Mensagem": "Item criado"}
@app.put("/items-atualizar/ {item_id}")
async def update_item(item_id:int, item:Item):
    conn = sqlite3.connect(BANCO)
    cur= conn.cursor()
    cur.execute("""UPDATE itens SET nome=? price=?, quantidade=? WHERE IF id=?""", (item.nome,item.price,item.quantidade,item_id))
    conn.commit()
    atualizado =cur.rowcount
    if atualizado:
        return {"mensagem": f"Item {item_id} atualizado."}
    return {"Erro": "Item não atualizado"}
