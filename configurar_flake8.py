

"""
Módulo:     configurar_flake8.py
Instalação: pip install flake8
"""

"------------------------------------------------ EXEMPLO CONFIGURAÇÃO ------------------------------------------------"
"OBS"  # lembrar sempre de separar arquivos e pastas por [ , ]
def exemplo():
    """
    [flake8]
    max-line-length = 120
    exclude =
        pythonbirds,
        entrevistas,
        pytools,
        outros arquivos,
        migrations,
        __pycache__,
        manage.py,
        settings.py
    """

"------------------------------------------------ TUTORIAL PARA PYTHON ------------------------------------------------"
def python():
    """
    - Criar uma pasta, um ambiente virtual e um arquivo [ .py ]
    - Ir ao terminal e executar: [ pip install flake8 ] e depois [ pip freeze > requirements.txt ]
    - Entrar no arquivo [ .py ] e inserir algum código que não condiga com a sintaxe da [ pep8 ]
    - Voltar ao terminal e executar: [ flake8 ]
    - A biblioteca verifica os arquivos dentro de onde ela foi instalada
    - Se há erros, mostra-se onde e qual o tipo dele
    """

"------------------------------------------------ TUTORIAL PARA DJANGO ------------------------------------------------"
def django():
    """
    - É basicamente a mesma coisa que no Python, porém em Django, costuma ter uma série de arquivos
    - Sendo assim, é preciso criar na raiz, um arquivo [ .flake8 ] para configurá-lo
    - Um exemplo de modelo foi descrito acima
    - Tirando isso, todos os procedimentos são os mesmos
    """
