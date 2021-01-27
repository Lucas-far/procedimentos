

"""
Módulo: postgresql_esconder_dados.py
Objetivo: inviabilizar nome, user, e senha do seu banco de dados
Palavra chave: esconder dados postgresql
"""

# Criar um projeto, seu ambiente virtual, e voltar ao Desktop
def parte1():
    """
    Abrir o terminal [ ctrl + alt + t ]
    cd Desktop
    mkdir postgresql_project
    cd postgresql_project
    python3 -m venv .venv
    cd ~
    """

# Criação de um usuário novo postgreSQL e torná-lo admin
def parte2():
    """
    sudo su - postgres
    psql
    CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    ALTER USER nome do usuário novo WITH SUPERUSER;
    \q
    exit
    """

# Criação de um servidor novo postgreSQL, passando os dados do usuário novo
def parte3():
    """
    Abrir o Pgadmin4
    Servers -> botão direito -> new -> server
    Aba [ general ] name=qualquer nome / nome do user criado acima
    Aba [ connection ] host=localhost / username=nome do user criado acima / password= senha do user criado acima
    """

# Criação de um bdd para usar no projeto, usando o usuário e seu servidor
def parte4():
    """
    Botão direito no servidor criado (ícone elefante) -> create -> database
    Aba [ general ] name=qualquer nome ----------------------------------------------------> OPÇÃO: dtb_nome_do_projeto
    Salvar
    Clicar no nome, para ativá-lo
    """

# Abrir o projeto no Pycharm, instalar dependências, pacote projeto, aplicação, e salvar dependências
def parte5():
    """
    Abrir o Pycharm -> menu -> file -> open
    git init
    pip install django==2.2.17 psycopg2-binary
    django-admin startproject pp .
    django-admin startapp pa
    pip freeze > requirements.txt
    """

# Criar os dois arquivos responsáveis por esconder seus dados
def parte6():
    """
    raiz/new/file/.gitignore ---------------------------------------------------------> adicionar texto [ dtb_data.py ]
    raiz/new/file/dtb_data.py
    """

# Conteúdo [ dtb_data.py ]
def parte7():
    """
    def show_dtb_name():
        return 'nome do seu bdd postgresql'

    def show_dtb_user():
        return 'nome da sua conta postgresql'

    def show_dtb_password():
        return 'sua senha postgresql'

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
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': f'{show_dtb_name()}',
            'USER': f'{show_dtb_user()}',
            'PASSWORD': f'{show_dtb_password()}',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    """

# Colheita dos arquivos do projeto para o Git, para vincular com o repositório remoto
def parte8():
    """
    git add .
    git commit -m 'first commit'
    -----------------------------------------------------------------------------> criar um repositório vazio no Github
    git remote add origin git@github.com:Lucas-far/test_postgresql.git
    git branch -M main
    git push -u origin main
    -----------------------------------------------------> atualizar a página do Github, onde está o repositório remoto
    ---------------------------> ir ao repositório remoto, atualizar a página, e ver se o arquivo ignorado está ausente
    """

"OBS"  # Quem clonar seu repositório, não terá acesso aos seus dados
"OBS"  # Mas também é preciso saber se o projeto está funcionando

# Testar se as funções estão, de fato, funcionando
def parte9():
    """
    Voltar ao terminal do projeto
    python manage.py shell
    from nome_seu_pacote_projeto.settings import DATABASES
    DATABASES
    -----------------------------------------------> as chaves [ NAME, USER, PASSWORD ] devem ter o retorno das funções
    exit()
    python manage.py migrate --------------------------------------------------------------------> não deve haver erros
    python manage.py runserver ------------------------------------------------------------------> não deve haver erros
    """
