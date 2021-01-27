

"""
Módulo: instalar_python_ubuntu.py
Objetivo: instalar e configurar python no OS Ubuntu
Palavra chave: instalar python ubuntu
"""

# Configuração de softwares úteis, não apenas o Python (apesar de ser o principal)
"Softwares"  # Java Development Kit / Python / Pycharm
def parte1():
    """
    1 ------------------------------------------------------------------------------------------------------------------
        FONTE 1: Java Archive Downloads - Java SE 11 - Oracle
        FONTE 2: https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html
        ARQUIVO: 04-jdk-11.0.7_linux-x64_bin.tar.gz
    1 ------------------------------------------------------------------------------------------------------------------

    2 ------------------------------------------------------------------------------------------------------------------
        FONTE: https://www.python.org/downloads/ ---> Acessar: Site / Downloads / All releases
        ARQUIVO: python-3.8.5.tar.xz             ---> versão muda de acordo com a época
    2 ------------------------------------------------------------------------------------------------------------------

    3 ------------------------------------------------------------------------------------------------------------------
        CONTA ORACLE: [ lu******2@g****.com ] [ W******s1* ]
        ARQUIVO: pycharm-community-2020.2.tar.gz
    3 -----------------------------------------------------------------------------------------------------------------
    """

# Configuração do Java DK
def parte2():
    """
    1 - Extrair o arquivo pela opção [ Extract here ]
    2 - Renomear diretório para [ jdk11 ] ---> se há módulos aninhados, leve todos para o diretório matriz
    3 - Ir para [ /home/seu_user/ ] e criar diretório [ apps ], ficando [ /home/seu_user/apps/ ]
    4 - ctrl + x em [ jdk11 ] para [ /home/seu_user/apps/ ]
    5 - Voltar para [ /home/seu_user ]
    6 - ctrl + h (mostrar módulos ocultos)
    7 - Procurar e abrir o diretório [ .bashrc ]
    8 - Ao final, adicionar as seguintes linhas de código:

        JAVA_HOME=/home/seu_user/apps/jdk11
        export JAVA_HOME
        PATH=$PATH:$JAVA_HOME/bin
        export PATH

    9 - Abrir o terminal e fazer [ java --version ]. O retorno deve ser a versão do Java
    """

# Atualizar os pacotes do Ubuntu
def parte3():
    """ sudo apt-get update """

# Instalar dependências essenciais
def parte4():
    """
    sudo apt-get install -y build-essential aria2 blt-dev curl gettext git libbz2-dev libffi-dev libgdbm-dev libjpeg-dev liblzma-dev libncurses5-dev libnss3-tools libreadline-dev libsqlite3-dev libssl-dev llvm python-dev python3-dev python3-venv sqlite3 tcl-dev tk-dev vim wget zlib1g-dev
    """

# Instalação e configuração do Python e seu gerenciador de pacotes: Pip
def parte5():
    """
    1 - Extrair o arquivo pela opção [ Extract here ]
    2 - Entrar na pasta extraida, e em uma área vazia da tela: [ botão direito -> open in terminal ]
    3 - No terminal: [ ./configure --enable-optimizations --with-ensurepip=install ]
    4 - No terminal: [ make -j 2 ]
    5 - No terminal: [ sudo make altinstall ]
    6 - No terminal: [ python 3 --version / python3.8 --version ]
    7 - No terminal: [ sudo apt update ] [ sudo apt install python3-pip ]
    8 - No terminal: [ pip --version ]
    9 - No terminal: [ pip install --upgrade pip ]
    """

# Configurar Virtualenv para o Python
def parte6():
    """
    1 - python -V (ctrl + c)
    2 - sudo pip(ctrl + v) install virtualenv virtualenvwrapper
    3 - Ir à rota [ /home/seu_user ]
    4 - mostrar módulos ocultos [ ctrl + h ], procurar e abrir [ .bashrc ]
    5 - Ao final, adicione as seguintes linhas de código:

        export WORKON_HOME=$HOME/.virtualenvs
        export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.8  # terminal: which python3.8
        source /usr/local/bin/virtualenvwrapper.sh

    6 - Será configurada uma rota: [ /home/seu_user/.virtualenvs ]
    7 - Nessa rota, são criados os ambientes virtuais gerados dos comandos:

        mkvirtualenv nome do av   # criação e login em um av
        deactivate                # deslogar de um av criado
        work on nome do av        # relogar em um av criado
        rmvirtualenv nome do av   # remover um av especificado

    --------------------------------------------------------------------------------------------------------------------
    OBS: Ambientes virtuais criados pelo [ virtualenv ] costumam vir ativados
    --------------------------------------------------------------------------------------------------------------------

    8 - E se for preciso fazer manualmente?

        - Supondo que haja um ambiente virtual em: [ /home/seu_user/.virtualenvs/ ]
        - Supondo que o nome do ambiente virtual seja: [ venv ]
        - Ir até a rota desse ambiente, manualmente ou usando o terminal
        - Sabendo a rota do diretório que guarda os ambientes e o nome do ambiente em si, então já se pode configurar
        - Em: /home/seu_user/.virtualenvs/
        - source z/bin/activate (para ativar)
        - deactivate (para desativar)
    """

# Instalar e configuração inicial do Pyenv
def parte7():
    """
    //////////////////////////////////////////////// INSTALAR/CONFIGURAR ///////////////////////////////////////////////

    1 - curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    2 - Ir à rota [ /home/seu_user/ ] e abrir o arquivo [ .bashrc ]
    3 - Inserir ao final:

        export PATH="/home/lucas/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"

    4 - Salvar [ .bashrc ] e reabrir o terminal
    5 - pyenv
    6 - pyenv install -l (listagem de versões para instalar do Pyenv)
    7 - Procurar na listagem, a versão inteiramente numérica mais atual [ EXEMPLO: 3.9.1 ]
    8 - Usar o comando de acordo com o exemplo acima: [ pyenv install 3.9.1 ]
    """

# Criar um ambiente virtual pelo Pyenv
def parte8():
    """
    - Crie uma pasta
    - Entre na pasta, e abrir esta no terminal
    - python3 -m venv .venv -------------------------------------------------------------------> criar ambiente virtual
    - source .venv/bin/activate --------------------------------------------------------------> ativar ambiente virtual
    - deactivate --------------------------------------------------------------------------> desativar ambiente virtual
    - ctrl + alt + del  ----------------------------------------------------> deletar ambiente virtual (após desativar)

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OBSERVAÇÕES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    venv  == parte do comando
    .venv == nome do ambiente virtual padrão
    """

# Atualizar um ambiente virtual
def parte9():
    """
    1 - pyenv install -l -----------------------------------------> verificar a versão inteiramente numérica mais atual
    2 - pyenv versions --------------------------------------------------------> retornar a versão python ativada no OS

    3 - Se 1 == 2

        Configure a versão python ativada mais atual ---------------------------------> [ EXEMPLO: pyenv global 3.9.1 ]

    4 - Caso contrário

        - Instalar versão numérica mais atual do item 3 -----------------------------> [ EXEMPLO: pyenv install 3.9.1 ]
        - Configurar a versão mais atual recem instalada como global ----------------> [ EXEMPLO: pyenv global 3.9.1  ]
    """

# Configuração do Pycharm
def parte10():
    """
    1 - Extrair o arquivo pela opção [ Extract here ]
    2 - Renomear para [ pycharm ]
    3 - Ir à rota [ /home/seu_user/apps ] (se não existe, criar)
    4 - [ ctrl + x ] o [ pycharm ] para [ /home/seu_user/apps/ ]
    5 - Entrar em [ /home/seu_user/apps/pycharm/bin ], e em uma área vazia: [ botão direito -> open in terminal ]
    6 - No terminal: [ sudo apt-get install alacarte -y ]
    7 - Ir ao Desktop, em [ Show applications ]
    8 - Procurar e abrir [ Main Menu -> Applications -> Programming -> New item -> Name: Pycharm ]
    8 - [ Command: /home/seu_user/apps/pycharm/bin/pycharm.sh ] [ Ícone: /home/lucas/apps/pycharm/bin/pycharm.png ]
    """

# Configuração essencial para criar projetos no Pycharm
def parte11():
    """
    1. Abrir o software
    2. Clicar em [ New Project ]
    3. Há duas formas de criar um projeto novo

       --------------------------------------------
       FORMA 1: Quando um ambiente não existe ainda
       --------------------------------------------

       1. Location = rota/nome do av
       2. New environment
              Base Interpreter
                  ...
                      /usr/local/bin/python3.8

       -------------------------------------
       FORMA 2: Quando um ambiente já existe
       -------------------------------------

       1. Location = rota/nome do av
       2. Existing Interpreter
              ...
                  Add Python Interpreter
                      /usr/bin/python3.8
    """
