#controller.py
from fastapi import APIRouter,Request,Form,UploadFile,File,Depends
#APIRouter=rota api para o front,
#requests = Requisição http,
# Form=Formulário para criar e editar,
# UploadFile= Upload da foto,
#File = Função para gravar caminho da imagem,
# Depends = Dependência do banco de dados sqlite
#pip install python-multipart

from fastapi.responses import HTMLResponse, RedirectResponse
#HTMLResponse= resposta do html get,post,put,delete
#RedirectResponse= redirecionar a resposta para o front 'index.html'
from fastapi.templating import Jinja2Templates
#jinja2Templates=responsáveis por renderizar o front-end
import os, shutil
#OS = funções de sistema,
#shutil= salva e puxa diretórios do sistema 'caminho das imagens'
from sqlalchemy.orm import Session
#Session= modelagem do ORM models
from database import get_db
#get_db= ingeção do SessionLocal na api
from models import Produto
#Produto = modelagem, nome, preco, quantidade, imagem
router= APIRouter()
templates = Jinja2Templates(directory="templates") #front-end
#pasta para salvar imagens
UPLOAD_DIR="Static/uploads"
#caminho para o os
os.makedirs(UPLOAD_DIR,exist_ok=True)
#rota para página inicial listar produtos
@router.get("/",response_class=HTMLResponse)
async def listar(request:Request, db:Session=Depends(get_db)):
    produtos = db.query(Produto).all()#puxar produtos do banco de dados
    return templates.TemplateResponse("index.html",{
        "request":request, "produtos":produtos
    })
#Rota detalhe do produto
@router.get("/produtos-get/{id_produto}",
            response_class=HTMLResponse)
async def detalhe(request:Request,id_produto:int,
                  db: Session=Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id==id_produto).first()
    return templates.TemplateResponse("produto.html",{
        "request":request,"produto":produto
    })