

# Requisito
def parte_1():
    """
    - O unittest já vêm configurado com o Python, portanto o requisito é a instalação do Python
    """

# Configuração
def parte_2():
    """
    - Recomenda-se criar um [ pacote python ], na raiz do seu repositório local, com o nome [ tests ]
    - Dentro do [ pacote tests ], gerar o nome dos arquivos de test, iniciando com [ test_.nome_complementar.py ]
    """

# Observações iniciais
def parte_3():
    """
    - No local onde for criado os testes, o [ unittest ] deve ser importado
    - No meu caso, eu faço programação estrutural, e crio algoritmos por métodos
    - É preciso importar esses métodos para o mesmo local onde o [ unittest ] é chamado
    """

# Exemplo
def parte_4():
    """
    - from unittest import TestCase

    from methods_database import (
        calculate_lifetime, customize_birthday, customize_birthday_str, find_sign, get_input_integer, instructions,
        should_algorithm_run, step_painter, welcome
    )
    """

# Forma de testar
""  # cria-se uma classe que herda [ TestCase ]
""  # o nome da classe, por convenção, deve ser [ Test + nome da função em camel case ]
""  # o teste resume-se em duas funções
""  # a primeira função, que deve receber o nome [ setUp ], configura variáveis que serão comparadas na segunda
""  # a segunda função, por convenção, deve ser [ test_ + nome da função ]
""  # no meu caso, minhas comparações são baseadas em [ assertEqual ] e [ assertNotEqual ]
def parte_5():
    """
    class TestCalculateLifetime(TestCase):

        def setUp(self) -> None:
            self.test_var = calculate_lifetime(year=1992, month=7, day=16)    # About 10426 days

        def test_calculate_lifetime(self) -> None:
            self.assertEqual(calculate_lifetime(1992, 7, 16), self.test_var)  # About 10426 days == About 10426 days
            self.assertNotEqual(calculate_lifetime(), self.test_var)          # About 737820 days != About 10426 days
    """

# Executar testes
def parte_6():
    """
    python -m unittest discover tests

    OBS: O comando baseia-se no fato de que você tenha, na raiz do seu projeto, um pacote com o nome: [ tests ]
    """
