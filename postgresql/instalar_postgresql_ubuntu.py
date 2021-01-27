

"""
Módulo: instalar_postgresql_ubuntu.py

Objetivo: utilizar bdd postgresql para poder usar em projetos Django no OS Ubuntu

Palavra chave: postgresql instalar ubuntu
"""

def fonte():
    """
    Curso # Banco de dados SQL e NoSQL - do básico ao avançado
    Seção # Seção 8:PostgreSQL - Parte 1
    Aula  # 75. Instalação e Configuração no Linux
    """

# Comandos utilitários antes da instalação
def parte1():
    """
    sudo apt update && sudo apt -y upgrade && sudo apt list --upgradable
    sudo reboot
    """

# Download e procedimentos iniciais de instalação do PostgreSQL
def parte2():
    """
    1 - Download -> https://www.postgresql.org/download/linux/ubuntu/
    1 - sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    2 - wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    3 - sudo apt-get update
    4 - sudo apt-get -y install postgresql-13

        COMANDO QUE PODE APARECER DURANTE A INSTALAÇÃO:
        4.1 - pg_ctlcluster 13 main start
    """

# Comandos em caso haja problemas em relação a parte 2
def parte3():
    """
    Se após os 3 comandos anteriores, haver um erro de arquitetura [ i386 ], então fazer os códigos

    Se   [ dpkg --print-foreign-architectures ] == i386, então continuar
    Se   [ dpkg --print-architecture ]          == amd64, então continuar
    Usar [ sudo dpkg --remove-architecture i386 ]
    """

# Download da interface gráfica do PostgreSQL
def parte4():
    """
    1 - sudo apt-get -y install pgadmin4
    """

# Comandos básicos relacionados os PostgreSQL
def parte5():
    """
    sudo su - postgres  # logar no postgresql com a conta padrão admin [ postgres ]
    psql                # usar o console psql em uma conta já logado [ no contexto: postgres ]
    help                # buscar comandos auxiliares
    \q                  # deslogar a conta
    exit                # deslogar do postgresql
    """

# Configurar uma senha para o usuário padrão [ postgres ]
"OBS"  # O segundo item 2 deve ter um retorno: ALTER ROLE
def parte6():
    """
    1 - sudo su - postgres
    2 - psql
    2 - ALTER user postgres WITH PASSWORD 'senha desejada';
    3 - \q
    4 - exit
    """

# Configurar um novo usuário, apartir do padrão [ postgres ]
def parte7():
    """
    1 - sudo su - postgres
    2 - psql
    3 - CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    4 - ALTER USER nome do usuário novo WITH SUPERUSER;
    5 - \q
    6 - exit
    """

# Deletar usuário não postgres (usuário não padrão)
def parte8():
    """
    1 - sudo su - postgres
    2 - dropuser nome_do_usuário
    """

# Deletar postgresql
def parte9():
    """
    1 - sudo apt-get --purge remove postgresql
    2 - dpkg -l | grep postgres
    3 - sudo apt-get --purge remove

        pgdg-keyring
        postgresql-12
        postgresql-13
        postgresql-client-12
        postgresql-client-13
        postgresql-client-common
        postgresql-common

    4 - EXEMPLO de como remover dependências em linha (baseado nos resultados acima)

        sudo apt-get --purge remove postgresql-12 postgresql-13 postgresql-client-12 postgresql-client-13 postgresql-client-common postgresql-common
    """
