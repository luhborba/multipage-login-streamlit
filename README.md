# Aplicação MultiPage com Controle de Acesso

O objetivo deste repositorio é aplicar controle de acesso em uma aplicação MultiPage no Streamlit. Utilizando um Exemplo fictissio chamado DataCollege-Borbs, simulando levemente uma plataforma de cursos, onde basicamente só temos 2 opções, cadastrar cursos e listar cursos. Apenas para exemplificar o uso de MultiPage com controle de acesso.

## Acessos

**Documentação:** [Git Pages com Documentação](https://luhborba.github.io/multipage-login-streamlit/)
**Aplicação:** [Link da Aplicação Web](https://datacollege-borbs.streamlit.app)

O usuários e senhas disponíveis estão no arquivo config.yaml.

## Stack Utilizada

- Python
- Streamlit
- Black
- Isort
- Pydocstyle
- Mkdocs
- Taskipy
- Streamlit-authenticator
- Mkdocs-material
- Mkdocstrings

## Clonando o Projeto com Poetry e Pyenv

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/multipage-login-streamlit.git
cd multipage-login-streamlit
```

2. Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Ativando Poetry
```bash
poetry env use 3.12.1
poetry shell
```

4. Insatalando dependências
```bash
poetry install --no-root
```

5. Rodando a Documentação
```bash
task doc
```

6. Rodando Aplicação
```bash
task run
```

## Clonando o Projeto pip e python-venv

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/multipage-login-streamlit.git
cd multipage-login-streamlit
```

3. Criando Ambiente Virtual
```bash
python -m venv .venv
```

4. Ativando Ambiente Virtual Windows
```bash
.venv/Scripts/activate
```

4. Ativando Ambiente Virtual Linux
```bash
source .venv/bin/activate
```

5. Instalando Dependencias
```bash
pip install -r requirements.txt
```

6. Rodando a Documentação
```bash
mkdocs serve
```

7. Rodando Aplicação
```bash
streamlit run app.py
```

## 📊 Conheça meu Canal do Canal no Youtube

<div style="display: flex; justify-content: center;">
  <div style="margin-right: 10px;">
    <a href="http://youtube.com/@luhborba?sub_confirmation=1">
      <img src="https://img.shields.io/youtube/channel/subscribers/UCN16u-GFjdNmVWlxBZvRqsQ" />
    </a>
  </div>
  <div style="margin-left: 10px;">
    <a href="http://youtube.com/@luhborba?sub_confirmation=1">
      <img src="https://img.shields.io/youtube/channel/views/UCN16u-GFjdNmVWlxBZvRqsQ" />
    </a>
  </div>
</div>

<h3 align="left">Conecte-se comigo:</h3>
<p align="left">
<a href="https://linkedin.com/in/luhborba" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="luhborba" height="30" width="40" /></a>
<a href="https://www.youtube.com/@luhborba" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="luciano borba" height="30" width="40" /></a>
</p>

