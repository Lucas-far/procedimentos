

"""
Módulo: instalar_mysql_windows.py
Objetivo: instalar MySQL para poder usar em projetos Django no OS Windows.
Palavra chave: mysql windows
"""

def fonte():
    """
    Curso # Banco de dados SQL e NoSQL - do básico ao avançado
    Seção # Seção 6:MySQL - Parte 1
    Aula  # 44. Instalação e Configuração no Windows
    """

# Onde achar
def parte1():
    """
    Google: download mysql windows 64 bit
    Link direto: https://dev.mysql.com/downloads/mysql/ (escolher Windows)
    """

# Procedimentos durante a instalação
def parte2():
    """
    1 - Na instalação, escolher instalação [ Custom ]
    2 - Na instalação customizada, baixar as seguintes ferramentas:

        MySQL Server 8.0.21 - x64
        MySQL Workbench 8.0.21 - x64
        MySQL Connector Python 8.0.21 - x64

    3 - Após o download, manter todas etapas como padrão
    4 - Criar uma senha para o usuário [ root ] padrão do servidor MySQL (faz parte da instalação)
    5 - Finalizar a instalação
    """

# Registrar o diretório bin do MySQL
def parte3():
    """
    1 - Ir à rota padrão de instalação do mysql no Windows, na pasta de binários
        ROTA:
             c:\program files\mysql\mysql server 8.0\bin [ ctrl + c ]

    2 - No windows, seguir os seguinte passos:

        Win
            este computador
                botão direito
                    propriedades
                        configurações avançadas do sistema
                            variáveis de ambiente
                                path
                                    editar
                                        novo
                                            c:\program files\mysql\mysql server 8.0\bin [ ctrl + v ]
    """

# Primeiro acesso pós instalação
def parte4():
    """
    1 - mysql -u root -p
    2 - mysql -uroot -p (se 1 falhar)

    3 - Se o mysql estiver devidamente configurado, será apresentado o MySQL Monitor
    4 - [ help ] para ter acesso a comandos de ajuda no MySQL Monitor
    5 - [ exit ] para deslogamento do MySQL Monitor
    """

"É preciso criar um usuário aparte do padrão, mas ela será criado através do padrão"

# Criação do usuário novo apartir do usuário admin padrão
def parte5():
    """
    1 - mysql -u root -p
    2 - mysql -uroot -p (se a primeira falhar)
    3. SHOW VARIABLES LIKE 'validate_password%';
    4. SET GLOBAL validate_password.policy=LOW;
    5. CREATE USER 'nome do usuário novo'@'localhost' IDENTIFIED BY 'senha desejada';
    6. GRANT ALL PRIVILEGES ON *.* TO 'nome do usuário novo' WITH GRANT OPTION;
    7. FLUSH PRIVILEGES;
    8. exit
    9. mysql -u nome do usuário novo -p
    9. mysql -unome do usuário novo -p (se o primeiro 9 não funcionar)
    10. digitar a senha do OS
    11. digitar a senha do usuário novo
    """

# Comandos pós login de uma conta
def parte6():
    """
    SHOW DATABASES;                # Mostrar uma lista de todos os bdds disponíveis
    USE nome do bdd;               # Logar em um dos bdds disponíveis
    SHOW TABLES;                   # Mostrar todas as tabelas criados pelo bdd alvo
    SELECT * FROM nome da tabela;  # Mostrar tabelas das tabelas de um bdd alvo
    """
