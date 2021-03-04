

"""
TUTORIAL SOBRE COMO CONFIGURAR PROJETO DJANGO COM BDD POSTGRESQL
"""

"----------------------------------------------------- INSTALAÇÃO -----------------------------------------------------"

""  # procedimentos / postgresql / instalar_postgresql_ubuntu
""  # procedimentos / postgresql / instalar_postgresql_windows

"---------------------------------------------- CONFIGURAÇÃO NO PGADMIN4 ----------------------------------------------"

"OBS"  # Por questão pessoal, eu acho que seja melhor criar uma conta para cada bdd postgresql criado
"OBS"  # Portanto, cada projeto que for usado postgresql, é melhor criar uma conta e depois criar o bdd nela


def criar_usuario_e_tornar_admin():
    """
    - sudo su - postgres
    - psql
    - CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    - ALTER USER nome do usuário novo WITH SUPERUSER;
    - \q
    - exit
    """
