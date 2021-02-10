

"""
Módulo: integracao_continua_com_travis_CI.py
Aula:   Integração Contínua com Travis CI
"""

"------------------------------------------------ EXEMPLO CONFIGURAÇÃO ------------------------------------------------"

"Configuração"           # criar na raiz (.travis.yml)
"flake8"                 # REQUISITOS (pip install flake8) (pip freeze > requirements.txt) (.flake8)
"pytest tests/tests.py"  # REQUISITOS (pip install pytest) (pip freeze > requirements.txt)
def exemplo():
    """
    language: python
    python:
      - "3.9"
    install:
      - pip install -r requirements.txt
    script:
      - flake8
      - pytest tests/tests.py
    """

"------------------------------------------------- DEFINIÇÃO: TRAVIS -------------------------------------------------"

# travis é uma integração contínua (continuous integration) para evitar execução de tarefas manuais reincidentes

"---------------------------------------------------- CRIAR CONTA ----------------------------------------------------"

def parte1():
    """
    1 - https://travis-ci.org/ ---> será mudado para o domínio [ https://travis-ci.com/ ]
    2 - Signup com sua conta GitHub

    MÉTODO 1:
    3 - https://travis-ci.org/getting_started
    4 - activate all repositories [ botão ]

    MÉTODO 2:
    3 - Na página inicial do Travis: [ avatar / settings ]
    4 - Ao carregar, você verá seus repositórios, ative aquele que você quer integrar ao Travis
    """

"-------------------------------------------------- ESCOLHER EMBLEMA --------------------------------------------------"
# Escolher um emblema para inserir em repositório local, no arquivo [ README.md ]
def parte2():
    """
    1 - Ir ao avatar / botão esquerdo / settings / clicar em um repositório
    2 - Procurar e clicar em uma borda de nome: [ build ]
    3 - Esta abrirá um [ Status Image ] com campos [ BRANCH ] [ FORMAT ] [ RESULT ]
    4 - No campo [ FORMAT ], escolher [ markdown ] e copiar o retorno do campo [ RESULT ]
    """
