

"""
TUTORIAL SOBRE COMO CONFIGURAR PROJETO DJANGO COM BDD MYSQL
"""

"----------------------------------------------------- INSTALAÇÃO -----------------------------------------------------"

""  # procedimentos / mysql / instalar_mysql_ubuntu
""  # procedimentos / mysql / instalar_mysql_windows

"------------------------------------------ CONFIGURAÇÃO NO MYSQL WORKBENCH -------------------------------------------"

""  # Abrir o MySQL Workbench
""  # É aberto de forma automática, um sheet para inserir alguma sintaxe de SQL
""  # --------------------------------------------------------------------------> Sintaxe: CREATE DATABASE nome_do_bdd;
""  # Clicar no ícone do raio para salvar o bdd criado
""  # Clicar em uma seta giratória chamada [ schema ] (lado esquerdo da tela)

"------------------------------------------------- PROJETO: TERMINAL --------------------------------------------------"

""  # pip install mysqlclient PyMySQL
""  # pip freeze > requirements.txt

"---------------------------------------------------- settings.py -----------------------------------------------------"


# NAME = nome do bdd especificado na sintaxe acima / USER = seu usuário / PASSWORD = senha do seu usuário
def var_databases():
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

"-------------------------------------------------------- raiz --------------------------------------------------------"

""  # Na raiz do projeto: [ raiz / new / python file / dtb_data.py ]
""  # Configurações do banco de dados estão no arquivo [ settings.py ], ficando expostas
""  # Existem maneiras de omitir arquivos, mas o arquivo [ settings.py ] não pode ser omitido
""  # Sendo assim, é melhor manter as informações de banco de dados em outro arquivo, que serão importados
""  # No aquivo [ dtb_data.py ] ficarão as funções que enviarão ao arquivo [ settings.py ], os dados de usuário
""  # Os dados ficam configurados no arquivo [ settings.py ], mas não são vistos
""  # Os dados ficam no arquivo [ dtb_data.py ], que pode ser omitido, e será

"---------------------------------------------------- dtb_data.py -----------------------------------------------------"


# if __name__ == '__main__' serve para testar as funções
def meu_modelo_de_funcoes():
    """
    def show_dtb_name():
        return 'nome do seu bdd mysql'


    def show_dtb_user():
        return 'nome da sua conta mysql'


    def show_dtb_password():
        return 'sua senha mysql'


    if __name__ == '__main__':
        print(show_dtb_name())
        print(show_dtb_user())
        print(show_dtb_password())
    """


"----------------------------------------------------- .gitignore -----------------------------------------------------"

""  # Com o arquivo alvo [ dtb_data.py ] configurado, este deve ser adicionado ao arquivo [ .gitignore ]


def adicionar_ao_gitignore():
    """ dtb_data.py """


"---------------------------------------------------- settings.py -----------------------------------------------------"


def reconfigurar_var_databases():
    """
    from dtb_data import *

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': f'{show_dtb_name()}',
            'USER': f'{show_dtb_user()}',
            'PASSWORD': f'{show_dtb_password()}',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    """


"------------------------------------------------------ terminal ------------------------------------------------------"

""  # É recomendável testar a variável [ DATABASES ], para ter certeza de que as chaves estão recebendo os valores


# Ao imprimir a variável, ela deve ter as chaves: [ NAME ] [ USER ] & [ PASSWORD ] preenchidas
def testar_var_databases_pelo_shell():
    """
    python manage.py shell
    from nome_seu_pacote_projeto.settings import DATABASES
    DATABASES
    """


"------------------------------------------------------ terminal ------------------------------------------------------"

""  # Se os comandos padrão de projeto não tiverem sido feitos, é melhor fazê-los


def comandos_padrao():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """
