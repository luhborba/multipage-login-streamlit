"""Página Inicial do Projeto."""
import streamlit as st


def home():
    """Página Inicial do Projeto."""
    st.title("Bem Vindo a Plataforma de Curso DataCollege-Borbs")
    st.image('data/logo.png')
    st.write(
        "Aqui você pode acessar custos com um preço acessivél. Aprenda no Melhor Lugar!!!!"
    )
    