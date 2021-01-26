

"""
Módulo: configurar_chave_ssh.py
"""

# Criar no OS, sua chave SSH pessoal, para usar no GitHub
def parte1():
    """
    1 - [ Ubuntu  ] ssh-keygen -t rsa
    1 - [ Windows ] ssh-keygen.exe -t rsa

    -------------------------------------------------------------------------------------------------------------------
    OBS: Em 1, eu creio que após "rsa", pode usar [ 'seu_email_github' ], mas não estou certo
    -------------------------------------------------------------------------------------------------------------------

    2 - Digitar uma passphrase

       EXEMPLO: umafrasepodevalermuitacoisamasaomesmotempopodenaovalernada

    --------------------------------------------------------------------------------------------------------------------
    OBS: Um diretório é criado em: [ /home/seu_user/.ssh ]
    --------------------------------------------------------------------------------------------------------------------

    3 - Serão criados: [ public key / key fingerprint = SHA256 / key's randomart ]
    4 - Ir ao diretório [ /home/seu_user/.ssh ], procurar por [ cat id_rsa.pub ], abrir e [ ctrl + c ]
    5 - Ir ao site do Github
    6 - Fazer o caminho: [ Avatar / Settings / SSH and GPG keys / New ssh key ]
    7 - No campo [ title ], dar o nome desejado à chave
    8 - No campo [ key ], [ ctrl + v ]
    9 - Salvar
    """
