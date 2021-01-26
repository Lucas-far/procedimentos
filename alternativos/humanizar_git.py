

c: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

print(texto := \
    f"""
    Git [ mãe ]
    
    Bebê
    {c[4]}    [ git init ]    {c[7]}
    
    Registro
    {c[4]}    [ git config --global user.name "seu_user" ] e [ git config --global user.email "seu_email" ]    {c[7]}
    
    Consulta do registro
    {c[4]}    [ git config user.name  ] e [ git config user.email ]    {c[7]}
    
    Criança 
    {c[4]}    [ git status ]    {c[7]}
    
    Adolescente 
    {c[4]}    [ git add. / git add arquivo.formato ]    {c[7]}
    
    ========== {c[3]}[ git add. / git add arquivo.formato ] pode ser encurtado dentro de [ git commit -am 'msg. obg.' ] pelo "a"{c[7]} ==========
    ========== {c[3]}Se um arquivo "adolescente" for editado, este volta a ser "criança"{c[7]} ==========
    
    Correção em um arquivo "adolescente" ou "criança"
    {c[4]}    [ git checkout nome_arquivo.formato' ]    {c[7]}
    
    Fazer um arquivo "adolescente" regressar a "criança" 
    {c[4]}    [ git reset HEAD nome_arquivo.formato ]    {c[7]}
    
    Adulto
    {c[4]}    [ git commit -m "msg. obg." ]    {c[7]}
    
    Diário do "arquivo adulto" contendo nome e qtd. de anotações
    {c[4]}    [ git shortlog -sn ]    {c[7]}
    
     Diário do "arquivo adulto" contendo nome, qtd. de anotações e títulos
    {c[4]}    [ git shortlog ]    {c[7]}
    
    Diário do "arquivo adulto" contendo nome, data, hora, e título das anotações de um arquivo do diário
    {c[4]}    [ git log --author="nome_user" ]    {c[7]}
    
    Diário do "arquivo adulto" contendo nome, data, hora e título das anotações
    {c[4]}    [ git log ]    {c[7]}
    
    Diário do "arquivo adulto" contendo nome, data, hora, título e local (caso localidade não padrão) das anotações
    {c[4]}    [ git log --decorate ]    {c[7]}
    
    Diário do "arquivo adulto" contendo nome, data, hora, título e gráficos das conexões entre anotações
    {c[4]}    [ git log --graph ]    {c[7]}
    
    Diário do "arquivo adulto" contendo nome, data, hora, título, destacando mudanças nas anotações com outra cor
    {c[4]}    [ git show código_commit ]    {c[7]}
    
    Quando um "arquivo adulto, adolescente ou criança" sofre alteração, seu(s) título(s) é/são exibido(s)
    {c[4]}    [ git diff --name-only ]    {c[7]}
    
    Quando um "arquivo adulto, adolescente ou criança" sofre alteração, seu título, local e modificações são exibidas
    {c[4]}    [ git diff ]    {c[7]} 
    
    Pegar uma ou mais páginas do diário, refazer algo no estado "adolescente"
    {c[4]}    [ git reset --soft código_commit ]    {c[7]}  
    
    Pegar uma ou mais páginas do diário, recortar, refazer algo no estado "criança", para depois ser colada de novo
    {c[4]}    [ git reset --mixed código_commit ]    {c[7]}   
    
    Rasgar uma ou mais páginas do diário, iniciando com uma outra igual
    {c[4]}    [ git reset --hard código_commit ]    {c[7]} 
    
    Adulto independente
    {c[4]}    [ git push ]    {c[7]}
    """)
