

""""""

"-------------------------------------------- INSTALAR E CONFIGURAR O GIT ---------------------------------------------"

""  # sudo apt-get install git-all
""  # git --version
""  # git config --global user.name 'nome_user_github'
""  # git config --global user.email 'email_user_github'

"---------------------------------------- VINCULAR REPOSITÓRIO REMOTO AO LOCAL ----------------------------------------"

""  # Ir ao Github e criar um repositório novo, sem os arquivos de configuração [ README.MD ] [ .gitignore ] [ LICENSE ]
""  # No seu OS, criar uma pasta
""  # Abrir a pasta criada em uma IDE (meu caso: Pycharm)
""  # git init
""  # git remote add origin link_ssh
""  # python3 -m venv .venv
""  # source .venv/bin/activate
""  # git add .
""  # git commit -m 'first commit'
""  # git branch -M main     OU     git branch -m main
""  # git push -u origin main

"------------------------------------ ADICIONAR ARQUIVOS RELEVANTES PÓS VINCULAÇÃO ------------------------------------"

""     # voltar ao github e criar um repositório novo apenas com os arquivos de configuração
""     # ao criar, entrar em cada um e copiar seus conteúdos, passando-os para o repositório principal
"OBS"  # os arquivos de configuração não foram adicionados na primeira etapa, para evitar conflitos de PUSH
""     # No arquivo [ .gitignore ], há outros arquivos adicionais, que podem ser inseridos ao topo:


# adicionar ao topo do arquivo
def adicionais_gitignore():
    """
    *.*~
    *.pyc
    """

"------------------------------------ CONFIGURAR UM ARQUIVO [ .gitignore ] GLOBAL -------------------------------------"

""  # Ir a rota [ /home/seu_user/ ], e criar arquivo [ .gitignore_global ]


def conteudo_do_arquivo_gitignore_global():
    """
    .idea/
    bin/
    *.sqlite3
    """


""  # Salvar, fechar e abrir o terminal
""  # git config --global core.excludesfile ~/.gitignore_global

"----------------------------------- CONFIGURAÇÔES PADRÃO PARA PROJETOS GLOBALMENTE -----------------------------------"

""  # django==2.2.17 (última versão LTS até o momento, portanto, recomendável)
""  # pytest      (não mandatório)
""  # coverage    (testes)
""  # model_mommy (testes)
def comandos_pip():
    """
    pip install django==2.2.17 django-bootstrap4 flake8 pytest model_mommy coverage

    terminal
    --------------------------------
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    python manage.py migrate
    python manage.py createsuperuser
    --------------------------------

    raiz
    ---------------------------------------------------
    raiz      / pa  / new       / directory / templates
    templates / new / html file / index
    raiz      / pa  / new       / directory / static
    static    / new / directory / css
    static    / new / directory / images
    static    / new / directory / js
    css       / new / file      / index.css
    js        / new / file      / scripts.js
    ---------------------------------------------------

    settings.py
    -------------------------------------
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = 'DIRS': ['templates']
    -------------------------------------

    urls.py
    --------------------------------------------
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    --------------------------------------------

    views.py
    -------------------------------------------------------
    from django.urls import path
    from .views import (
        IndexTemplateView
    )

    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index')
    ]
    -------------------------------------------------------

    pa/urls.py
    ---------------------------------------------
    from django.shortcuts import render
    from django.views.generic import TemplateView

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'
    ---------------------------------------------
    """


"------------------------------------------------- CONFIGURAR FLAKE8 --------------------------------------------------"

""  # Criar na raiz do projeto, um arquivo [ .flake8 ]

def configurar_flake8():
    """
    ---------------------
    [flake8]
    max-line-length = 120
    exclude =
        migrations,
        __pycache__,
        manage.py,
        settings.py
        .venv
    ---------------------
    """


""  # Após a configuração, pode ser realizado um teste usando, no terminal, o comando: [ flake8 ]

"-------------------------------------------------- CONFIGURAR PYUP ---------------------------------------------------"

""  # O pyup analisa seus repositórios (normalmente em Github), para manter suas dependências instaladas, atualizadas
""  # O primeiro passo é ir ao website do pyup [ https://pyup.io/ ] para vincular sua conta Github
""  # Tendo os seus repositórios já vinculados, selecione um deles, para que o Pyup possa verificar
""  # Se há dependências desatualizadas, estas serão destacadas,
""  # As dependências desatualizadas terão um botão [ PR = PULL REQUEST ] que pode ser enviado ao repositório alvo

"OBS"  # Um arquivo na raiz também pode ser configurado, mas não sei explicar exatamente como é sua configuração
"OBS"  # O nome do arquivo deve ser [ .pyup.yml ]
"OBS"  # Não é recomendável usar repositórios privados em relação ao [ Pyup ]

"----------------------------------------------- CONFIGURAÇÃO DO PYTEST -----------------------------------------------"

""  # A instalação pode ser pulada, pois eu acho a próxima configuração melhor (coverage)
""  # É necessário a instalação da biblioteca: [ pip install pytest ]
""  # É recomendável a configuração da biblioteca como padrão
""  # File -> Settings -> Tools -> Python Integrated Tools -> Default test runner = pytest
""  # No projeto: [ raiz / new / python package / tests ]
""  # Exemplos de arquivos para o pacote: [ test_models.py ] [ test_views.py ] [ test_forms.py ] [ tests.py ]
""  # [ tests.py ] é um tipo de arquivos mais destinado a funções normais


def modelo_para_funcoes_normais():
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


""  # No terminal, executar: [ pytest local_dos_arquivos ], por exemplo [ pytest tests/test.py ]

"---------------------------------------------- CONFIGURAÇÃO DO COVERAGE ----------------------------------------------"

""  # Coverage é uma biblioteca feita para testes de arquivos, normalmente existentes no pacote aplicação
""  # Apesar de já ter sido instalado acima, é melhor deixar um lembrete: [ pip install coverage model_mommy ]

def configurar_pastas_e_arquivo_coverage():
    """
    ---------------------------------------------
    raiz  / new / python package / tests
    tests / new / python file    / test_models.py
    tests / new / python file    / test_views.py
    tests / new / python file    / test_forms.py
    raiz  / new / file           / .coveragerc
    ---------------------------------------------

    Configuração do arquivo [ coveragerc ]
    --------------------------------------
    [run]
    source = .

    omit =
        */__init__.py
        */settings.py
        */manage.py
        */wsgi.py
        */apps.py
        */urls.py
        */admin.py
        */migrations/*
        */tests/*
        .venv/*
        htmlcov/* (opcional, ainda não existente)
    --------------------------------------
    """


""  # Apenas a criação de arquivos de teste não faz sentido, se não há ferramentas a serem testadas
""  # Como exemplo, vamos usar um modelo para exemplificar um teste


def configurar_modelo_para_exemplificar_teste():
    """
    models.py
    -----------------------------------------------------
    class ModeloApenasParaTeste(models.Model):
        texto = models.CharField('Texto', max_length=500)

        class Meta:
            verbose_name = 'Texto'
            verbose_name_plural = 'Textos'

        def __str__(self):
            return self.texto
    -----------------------------------------------------

    admin.py
    -----------------------------------------
    from .models import ModeloApenasParaTeste
    @admin.register(ModeloApenasParaTeste)
    class ModeloAdmin(admin.ModelAdmin):
        list_display = ('texto',)
    -----------------------------------------


    COMANDOS PÓS CRIAÇÃO DE MODELOS
    ---------------------------------
    - python manage.py makemigrations
    - python manage.py migrate
    ---------------------------------


    - Note que não é preciso importar os modelos, apenas o model_mommy, que chama o modelo como argumento
    - .texto = campo do modelo [ ModeloApenasParaTeste ]


    tests/test_models.py
    --------------------------------------------------------
    from django.test import TestCase
    from model_mommy import mommy

    class ModeloApenasParaTesteTestCase(TestCase):
        def setUp(self):
            self.var = mommy.make('ModeloApenasParaTeste')

        def test_modelo_apenas_para_teste(self):
            self.assertEquals(str(self.var), self.var.texto)
    --------------------------------------------------------


    COMANDOS CAVERAGE MAIS ÚTEIS
    ----------------------------------------------------------------------------------------------
    - coverage run manage.py test
    - coverage report        || consulta rápida de progresso, sem detalhes
    - coverage html          || consulta analítica, para ver detalhes melhores dos erros
    - python -m http.server  || acesso à consulta analítica pelo navegador, pela pasta [ htmlcov ]
    - rm -rf htmlcov         || deletar após ter um progresso, para recriar com o progresso novo
    ----------------------------------------------------------------------------------------------


    LÓGICA RELACIONADA AO COVERAGE
    --------------------------------------------------------------------------------------------------------------------
    - A cada tentativa de conserto, executa-se em conjunto: [ coverage run manage.py test ] depois [ coverage report ]
    - Se o erro for consertado:                             [ rm -rf htmlcov ]
    --------------------------------------------------------------------------------------------------------------------


    OUTRO EXEMPLO, TESTANDO UMA FUNÇÃO NORMAL
    -----------------------------------------------------
    from django.test import TestCase

    def remover_vogais(string):
        container = []

        vowels = ['a', 'e', 'i', 'o', 'u',
                  'à', 'á', 'â', 'ã',
                  'é',
                  'í',
                  'ó', 'ô', 'õ', 'ò'
                  'ú',
                  ]

        for lt in string:
            container.append(lt)
        for lt in vowels:
            while lt in container:
                container.pop(container.index(lt))
        container = ''.join(container)
        return container

    class FirstTestCase(TestCase):
        def setUp(self):
            self.texto = 'Lucas Farias Santos de Sousa'

        def test_remover_vogais(self):
            frase = remover_vogais(self.texto)
            self.assertTrue(frase == 'Lcs Frs Snts d Ss')
    -----------------------------------------------------
    """

"----------------------------------------------- CONFIGURAÇÃO DO TRAVIS -----------------------------------------------"

# Recomenda-se ser a última instância a ser configurada, devido os scripts terem que rodar ferramentas já configuradas
def configurar_travis_ci():
    """
    - Ir ao website do [ Travis CI ] e vincular sua conta Github com a ferramenta
    - Após o vinculamento, é preciso ir à página onde estão seus repositórios
    - Clique no seu avatar (normalmente no lado direito e superior da tela) e clique em [ settings ]
    - Clique no nome do repositório que você quer fazer a integração
    - Volte ao seu projeto e criar um arquivo em sua raiz, chamado [ .travis.yml ]

    --------------------------------------------------- configuração ---------------------------------------------------
        language: python
        python:
          - "3.9"
        install:
          - pip install -r requirements.txt
        script:
          - flake8
    --------------------------------------------------------------------------------------------------------------------

    - No item [ script: ], dependendo da extensão do seu projeto, podem ser adicionados ações variadas

    ----------------------------------------------- exemplos de scripts ------------------------------------------------
    script:
      - flake8
      - pytest tests/tests.py
    --------------------------------------------------------------------------------------------------------------------

    - Porém, a execução de uma build do seu repositório, requer procedimentos extras

    ------------------------------------------------------ EXTRAS ------------------------------------------------------
    - A build é iniciada no site após efetuar um PUSH, feito após a configuração do arquivo [ .travis.yml ],
    - A página executará o que foi escrito na configuração
    - Pode-se adicionar emblemas ao arquivo [ README.MD ] do seu projeto, pela página da sua build
    - Há um ícone clicável chamado [ build ], e ao clique, seu link para [ markdown ] pode ser copiado
    - Vá ao seu projeto, no arquivo [ README.MD ] e cole este link, salve
    """
