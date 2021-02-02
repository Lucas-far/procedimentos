

"""
Módulo: configurar_flake8.py
Objetivo: analisar se um código/projeto segue as práticas da pep8 do Python
Instalação: pip install flake8
"""

def python():
    """
    1 - Criar um projeto (um diretório com um ambibente virtual)
    2 - Criar qualquer arquivo [ .py ] com algum código erro de sintaxe de acordo com a [ pep8 ]
    3 - No terminal: flake8
    4 - Se não há erro(s), não há retorno
    """

def django():
    """
    1 - Entre no seu projeto
    2 - Na raiz, criar um arquivo: [ .flake8 ]
    3 - Adicionar as seguintes linhas:

        [flake8]
        max-line-length = 120
        exclude =

          .nome_do_ambiente_virtual

          ADICIONAIS PARA PROJETO
          migrations
          __pycache__
          manage.py
          settings.py

    4 - No terminal: flake8
    5 - Todos os arquivos serão analizados, com exceção das opções salvas no arquivo: [ .flake8 ]
    """
