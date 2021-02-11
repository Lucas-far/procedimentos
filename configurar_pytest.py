

# Instalar
def parte_1():
    """
    - pip install pytest
    - pip freeze > requirements.txt
    - pytest tests

    OBS: O comando 3 baseia-se no fato de que você tenha, na raiz do seu projeto, um pacote com o nome: [ tests ]
    """

# Registros contextuais
def parte_2():
    """
    PROBLEMAS
    - Na aula de exemplo, o professor fez [ pytest nome_do_pacote ]
    - A sintaxe parece correta, pois eu faço o mesmo, mas comigo, nesse contexto, não deu certo
    - Eu tive que usar o terminal para entrar onde estavam os arquivos de teste
    - Para então poder fazer [ pytest 'nome_do_arquivo.py' ]
    """

# Configuração do [ Pytest ] no [ Pycharm ]
"OBS"  # para que a configuração possa ser feita, o pytest deve ter sido instalado
def parte_3():
    """
    File -> Settings -> Tools -> Python Integrated Tools -> Default test runner = pytest

    EXECUTAR TESTE
        - botão direito no arquivo [ .py ] de teste (igual Unittest)
        - [ pytest tests/tests.py ] TRADUÇÃO [ pytest nome do pacote/nome do arquivo de testes ]
    """

# Exemplo de testes
def parte_4():
    """
    def make_dict(chave, valor):
        return {chave: valor}

    def test_make_dict():
        assert make_dict('chave', 'valor') == {'chave': 'valor'}

    def turn_list_into_str(list_items: list):
        return "".join(list_items)

    def test_turn_list_into_str():
        assert turn_list_into_str(['123']) == '123'
    """
