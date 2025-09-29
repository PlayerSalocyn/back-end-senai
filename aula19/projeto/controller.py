#controller.py
'''
api router para ligar o back-end com o front-end //
criar uma rota da api para redirecionar para o html
'''
#import api rota, redirecionar para o html
from fastapi import APIRouter, Depends, Request, Form
#Request = requisição http// Dependes é o método GET, POST, PUT, DELETE
#import conexão do orm
from sqlalchemy.orm import Session
#import conexão com o database
from database import sessionLocal
#import do models manipulação nome e email do usuário
from models import sessionLocal, Usuario
#import resposta do html método http
from fastapi.responses import HTMLResponse,RedirectResponse
#motor gráfico do template, renderizar html,css, javascript
#pip install jinja2
from fastapi.templating import Jinja2Templates
#criar uma variável responsável pelas rotas da api
router=APIRouter()
#configurar o template do front-end
templates = Jinja2Templates(directory="view") #pasta o html
#função para abrir e fechar sessão com o banco de dados
def get_db():
    db= sessionLocal() #conexão com o banco de dados sqlite
    try:
        yield db #yield coletar o banco de dados
    finally:
        db.close() #finaliza a função, fechando a conexão
# Rota inicial (redirecionar o get da api para o index.html)
@router.get("/",response_class=HTMLResponse)
#função para fazer request na api trazer os dados do banco e redirecionar para o html 'front-end'
async def home(request:Request,db:Session=Depends(get_db)):
    #buscar todos os usuários do banco de dados
    usuarios= db.query(usuarios).all()
    #retornar os dados para a pégina html 'index.html'
    return templates.TemplateResponse("index.html",{
        "request":request, "usuarios":usuarios
    })

@router.get('/novo', response_class=HTMLResponse)
async def novo_usuario(request:Request):
    return templates.TemplateResponse("novo.html",
                                      {"request":request})
#rota post criar usuário (POST)
@router.post("/criar")
async def criar_usuario(nome:str=Form(...),
                        email:str=Form(...),
                        db: Session=Depends(get_db)):
    #models
    usuario = Usuario(nome=nome,email=email)
    db.add(usuario)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
    #303 código http redirecionamento de página
#rota formulário e edição
@router.get("editar/{usuario_id}", response_class=HTMLResponse)
async def editar_usuario(usuario_id: int, request: Request,
                         db: Session=Depends(get_db)):
    #models
    usuario = db.query(Usuario).filter(Usuario.id=usuario_id).first
    return templates.TemplateResponse("editar.html",
                                      {"request":request, "usuario":usuario})
@router.post("/atualizar/{usuario_id}")
async def criar_usuario(usuario_id:int, nome:str=Form(...),
                        email:str=Form(...),
                        db: Session=Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id=usuario_id).first
    usuario.nome=nome
    usuario.email=email
    db.add(usuario)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
    