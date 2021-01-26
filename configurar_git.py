

"""
Módulo: configurar_git.py
"""

# Configurar dados para que o Git conecte você ao GitHub
def parte1():
    """
    git config --global user.name 'nome_user_github'
    git config --global user.email 'email_user_github'
    git config --global core.editor nome_ide                                   (normalmente não feito, mas é bom saber)
    git config -l
    """

# Configuração de um arquivo [ .gitignore ] global
def parte2():
    """
    1 - Ir a rota [ /home/seu_user/ ], local recomendado para criar o arquivo git
    2 - Criar arquivo [ .gitignore_global ]
    3 - Inserir:

        .idea/
        bin/
        *.sqlite3

    4 - Salvar e fechar. Entrar no terminal
    5 - git config --global core.excludesfile ~/.gitignore_global
    """
