

"""
Módulo: postgresql_config_pycharm_python.py
Objetivo: configurar bdd postgreSQL dentro de um projeto Django
Palavra chave: postgresql no projeto
"""

"Título"  # Criação de um usuário novo
"OBS"     # Por questão pessoal, eu decide que é melhor criar uma conta para cada bdd postgresql criado
"OBS"     # Portanto, cada projeto que for usado postgresql, é melhor criar uma conta e depois criar o bdd nela
def terminal():
    """
    1 - sudo su - postgres
    2 - psql
    3 - CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    4 - ALTER USER nome do usuário novo WITH SUPERUSER;
    5 - \q
    6 - exit
    """

"Título"  # Criação de um servidor
"OBS"     # Por questões pessoais, eu criei um servidor: [ dernutzer1 ]
"OBS"     # A intenção disso é manter essa ordem, aumentando apenas o inteiro, a cada novo projeto que use postgresql
def pgadmin():
    """
    1 - Abrir o Pgadmin4
    2 - Servers -> botão direito -> new -> server
    3 - Uma janela nova abrirá
    4 - Aba [ general ] name=qualquer nome / nome do user criado acima
    5 - Aba [ connection ] host=localhost / username=nome do user criado acima / password= senha do user criado acima
    """

"Título"  # Criação de um bdd
def pgadmin_():
    """
    Botão direito no servidor criado (ícone elefante) -> create -> database
    Aba [ general ] name=qualquer nome
    Salvar
    Clicar no nome, para ativá-lo
    """

# Dependência necessária para usar PostgreSQL em um projeto Django
def terminal2():
    """
    1. pip install psycopg2-binary
    2. pip freeze > requirements.txt
    """

"OBS"  # NAME USER PASSWORD = servidor / username da conta nova / senha da conta nova
def settings():
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    """

def deploy_heroku():
    """
    1  - pip install dj-database-url
    2  - pip freeze > requirements.txt
    3  - import dj_database_url
    4  - Comentar DATABASES
    5  - DATABASES = {'default': dj_database_url.config()}
    6  - git init
    7  - git status
    8  - git add .
    9  - git commit -m "deploy_initial_config" (repetir, caso demore demais...)
    10 - git status
    11 - heroku login
    12 - heroku create av.sufixo desejado --buildpack heroku/python
    13 - git push heroku master
    14 - heroku run python manage.py migrate
    15 - heroku run python manage.py createsuperuser
    """
