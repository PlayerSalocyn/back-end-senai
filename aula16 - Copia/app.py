#aula16 MVC



'''
Conceito de MVC com o streamlit

estrutura do APP
meu_app//
models/usuario.py #model(ORM)
controllers/usuario_controller.py #Controller python base
app.py #View (streamlit)
database.py #Configuração do bano de dados sqlite

MVC (Model-View-Controller) é um padrão de arquitetura usado
no desenvolvimento de software, incluindo Python, para separar
uma aplicação em três componentes distintos:

Model (Modelo): Este componente manipula os dados e a lógica de
negócios da aplicação. Ele interage com o banco de dados
(ou outras fontes de dados), armazena e recupera dados e
garante a integridade dos dados.
Em frameworks web Python, os modelos são frequentemente
implementados usando Mapeadores Objeto-Relacionais (ORMs)
para representar tabelas de banco de dados como objetos Python.

View (Visualização): Este componente é responsável pela camada
de apresentação, ou seja, o que o usuário vê e com o qual
interage. Ele exibe dados do Modelo e fornece a
interface do usuário. Em aplicações web, isso
normalmente envolve HTML, CSS e JavaScript,
frequentemente renderizados usando mecanismos de modelagem.

Controller (Controlador): Este componente atua como um
intermediário entre o Modelo e a Visão. Ele recebe a
entrada do usuário (por exemplo, solicitações de um
navegador da web), processa a entrada,
interage com o Modelo para executar operações e, em
seguida, atualiza a Visão para refletir as alterações.
'''



import streamlit as st
from controller.usuario_controller import criar_usuario,listar_usuarios,atualizar_usuario,deletar_usuario

st.title("Usuários MVC (ORM + python + streamlit)")

st.subheader("Adicionar Usuário")
nome = st.text_input("Nome: ")
email = st.text_input("email: ")
if st.button("Salvar"):
    criar_usuario(nome, email)
    st.success("Usuário cadastrado")
#listar usuário
st.subheader("Usuários cadastrados")
usuario=listar_usuarios()
for i in usuario:
    st.write(f"ID: {i.id} Nome: {i.nome} Email: {i.email}")

st.subheader("Atualizar e deletar usuário.")
usuario=listar_usuarios()
if usuario:
    for i in usuario:
        with st.expander(f"{i.nome} {i.email}"):
            novo_nome= st.text_input('Novo nome:',
                                     value=i.nome,
                                     key=f"nome:{i.id}")
            novo_email= st.text_input('Novo email: ',
                                     value=i.email,
                                     key=f"email:{i.id}")
            col1,col2 = st.columns(2)
            with col1:
                if st.button("Atualizar", key=f"Update: {i.id}"):
                    atualizar_usuario(i.id, novo_nome, novo_email)
                    st.success("Usuário atualizado")
                    #recarregar a página
                    st.experimental_rerun()
            with col2:
                if st.button("Deletar", key=f"Deletar:{i.id}"):
                    deletar_usuario