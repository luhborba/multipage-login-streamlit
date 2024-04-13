"""Arquivo principal do Streamlit."""
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from paginas.criar_cursos import form_curso
from paginas.home import home
from paginas.listar_cursos import listar

st.set_page_config(page_title="DataCollege - Borbs", page_icon="🏫", layout="wide")

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.sidebar.title("Páginas")
    st.sidebar.write(f'Bem Vindo *{st.session_state["name"]}*')
    paginas = st.sidebar.selectbox(
        "Selecione uma página", ("Home", "Lista de Cursos", "Criar Curso", "Ajuda")
    )

    if paginas == "Home":
        home()
    elif paginas == "Criar Curso":
        form_curso()
    elif paginas == "Lista de Cursos":
        listar()
    else:
        st.write("Ainda Estou desenvolvendo")


elif st.session_state["authentication_status"] is False:
    st.error("Usuário/Senha is inválido")
elif st.session_state["authentication_status"] is None:
    st.warning("Por Favor, utilize seu usuário e senha!")
