

"""
Módulo: instalar_postgresql_windows.py

Objetivo: configurar bdd postgresql para poder usar em projetos Django no OS Windows

Palavra chave: postgresql instalar windows
"""

def fonte():
    """
    Curso # Banco de dados SQL e NoSQL - do básico ao avançado
    Seção # Seção 8:PostgreSQL - Parte 1
    Aula  # 74. Instalação e Configuração no Windows
    """

# Onde achar e fazer download (64 bits)
def parte1():
    """
    1 - https://www.postgresql.org/download/windows/
    """

# Ferramentas no instalador, a serem baixadas
def parte2():
    """
    1 - PostgreSQL server
    2 - Pgadmin4
    3 - Stack Builder
    4 - Command line tools
    5 - Também será requisitado a configuração de uma senha para o usuário admin padrão [ postgres ]
    """

# Configuração dos binários
def parte3():
    """
    1. Ir à rota padrão de instalação do postgresql no Windows, na pasta bin
       ROTA (copiar) (ctrl + c):
                                c:\Program Files\PostgreSQL\12\bin

    2. No windows, seguir os seguinte passos:
       Win
           este computador = pesquisar
                botão direito
                    propriedades
                        configurações avançadas do sistema
                            variáveis de ambiente
                                path
                                    editar
                                        novo

    3. Colar a rota da pasta binária:
                                     c:\Program Files\PostgreSQL\12\bin
    """

# Testar se o PostgreSQL foi configurado com sucesso
def parte4():
    """
    1. psql -U postgres
    2. Inserir senha do usuário admin [ postgres ]
    3. O terminal retornará o Console psql

    OBSERVAÇÕES:
                4. Porém a melhor maneira de uso do PostgresSQL é pela sua aplicação web [ Pgadmin4 ]
                5. Pgadmin4 é instalado durante a instalação do software postgresql
    """

# Configuração da interface gráfica do PostgreSQL
"OBS"  # Software instalado durante a instalação do PostgreSQL (parte 2)
def parte5():
    """
    1. Abrir o software [ Pgadmin4 ]
    2. Na abertura, sempre será requisitado a senha da sua conta Windows

    3. Ao fornecer a senha criada:
       Servers
           PostgreSQL (nome padrão inicial do primeiro servidor)
               digitar senha do usuário [ postgres ] criado na instalação
    """

# Criação do usuário novo, apartir do padrão [ postgres ]
def parte6():
    """
    1. Após as duas requisições, torna-se disponível:
       Login/Group Roles
           botão direito
               create
                   login/group role...
                       general
                           name = nome do usuário novo
                               definition
                                   password = senha do usuário novo
                                       privilegies
                                           Can login = Yes
                                               Superuser = Yes
                                                   save
    """

# Configuração do servidor novo, não padrão
def pgadmin4_parte3():
    """
    ALTERNATIVO: deletar servidor padrão

        Browser
            Servers
                PostgreSQL 12
                    botão direito
                        remove server
                            yes

    CRIAÇÃO DE UM SERVIDOR NOVO

        Browser
            Servers
                botão direito
                    Create
                        Server
                            General
                                name = dê um nome ao servidor
                                    Connection
                                        host = localhost
                                        username = nome do usuário criado em [ Login/Group Role... ]
                                        password = senha do usuário criado em [ Login/Group Role... ]
                                            save
    """
