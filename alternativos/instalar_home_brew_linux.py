

"""
Módulo: instalar_home_brew_linux.py
Objetivo: instalar dependências diversas para Linux
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 8:Trabalhando com tradução de projetos
    Aula:   # 73. Instalando e configurando o gettext - Linux
    """

"OBS"  # Site do Homebrew e guia de instalação - https://brew.sh/

# Instalação
def parte1():
    """
    1 - /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    2 - echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >> /home/lucas/.profile
    3 - eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
    4 - brew                                                                        (verificar se o brew foi instalado)
    5 - brew install gettext                                                                (usado no contexto da aula)
    6 - brew link gettext --force                                                           (usado no contexto na aula)
    """

# Ferramenta não origatória (tradutor), mas pode ser importante, dependo do contexto de trabalho
def parte2():
    """
    1 - https://poedit.net/
    2 - sudo snap install poedit
    """

# Comandos relacionados ao Brew
def parte3():
    """
    1 - brew install wget gcc
    2 - brew install gcc
    3 - sudo apt-get install -y build-essential gettext (importante, não lembro a razão)
    4 - sudo apt-get update -y
    """
