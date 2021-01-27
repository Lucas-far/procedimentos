

"""
Módulo: mysql_esconder_dados.py
Objetivo: inviabilizar nome, user, e senha do seu banco de dados
Palavra chave: esconder dados mysql
"""

# Criar um projeto, seu ambiente virtual, e voltar ao Desktop
def parte1():
    """
    Abrir o terminal [ ctrl + alt + t ]
    cd Desktop
    mkdir mysql_project
    cd mysql_project
    python3 -m venv .venv
    exit
    """

# Criação do bdd
def parte2():
    """
    Abrir o MySQL Workbench
    CREATE DATABASE dtb_mysql_project;
    """

# Abrir o projeto no Pycharm, instalar dependências, pacote projeto, aplicação, e salvar dependências
def parte3():
    """
    Pycharm / File / Open
    git init
    pip install django==2.2.17 mysqlclient
    django-admin startproject pp .
    django-admin startapp pa
    pip freeze > requirements.txt
    """

# Criar os dois arquivos responsáveis por esconder seus dados
def parte4():
    """
    raiz/new/file/.gitignore ---------------------------------------------------------> adicionar texto [ dtb_data.py ]
    raiz/new/file/dtb_data.py
    """

# Conteúdo [ dtb_data.py ]
def raiz():
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

# Configuração do bdd
def pp_settings():
    """
    from dtb_data import show_dtb_name, show_dtb_user, show_dtb_password

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

# Colheita dos arquivos do projeto para o Git, para vincular com o repositório remoto
def parte5():
    """
    git add .
    git commit -m 'first commit'
    ---------------------------------------------------------------------------> criar um repositório vazio no Github
    git remote add origin git@github.com:Lucas-far/test_mysql.git
    git branch -M main
    git push -u origin main
    -----------------------------------------------------> atualizar a página do Github, onde está o repositório remoto
    ---------------------------> ir ao repositório remoto, atualizar a página, e ver se o arquivo ignorado está ausente
    """

"OBS"  # Quem clonar seu repositório, não terá acesso aos seus dados
"OBS"  # Mas também é preciso saber se o projeto está funcionando

# Testar se as funções estão, de fato, funcionando
def parte6():
    """
    Voltar ao terminal do projeto
    python manage.py shell
    from nome_seu_pacote_projeto.settings import DATABASES
    DATABASES
    ---------------------------------------> as chaves [ NAME, USER, PASSWORD ] devem ter o retorno das funções
    exit()
    python manage.py migrate ------------------------------------------------------------------> não deve haver erros
    python manage.py runserver ----------------------------------------------------------------> não deve haver erros
    """
