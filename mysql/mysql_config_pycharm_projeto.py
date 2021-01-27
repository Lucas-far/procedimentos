

"""
Módulo: mysql_config_pycharm_projeto.py
Objetivo: configurar um projeto para receber um bdd mysql
Palavra chave: mysql no projeto
"""

# Criação do bdd anteriormente a configuração do projeto
def mysql_workbench():
    """
    1 - Logar no usuário novo [ instalar_mysql_windows.py ] ou [ instalar_mysql_ubuntu.py ]
    2 - Inserir a senha do usuário novo
    3 - CREATE DATABASE nome_do_bdd;
    4 - Clicar no ícone do raio
    5 - Clicar na seta giratória perto da aba [ schema ]
    """

# Dependência para integração do MySQL com o projeto que vai usá-lo
"OBS"  # talvez a segunda dependência da linha 1 não seja necessária
def parte1():
    """
    1 - pip install mysqlclient PyMySQL
    2 - pip freeze > requirements.txt
    """

# Configuração do banco de dados
def pp_settings():
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nome_do_bdd',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    """
