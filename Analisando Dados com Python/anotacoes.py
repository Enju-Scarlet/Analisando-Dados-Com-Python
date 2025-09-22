# Usaremos uma extensão de arquivo diferente, no caso o .ipynb
# .ipynb é um notebook do júpiter
    # Nele podemos adicionar células de códigos;
    # Normalmente em projetos de dados, é comum usá-lo, pois fazemos uma célula, a rodamos e vemos o resultado.

# No canto superior direito iremos selecionar o nosso Kernel (Núcleo) como Python

# Primeira coisa que deveremos fazer é o Passo a Passo (Pensando em Português)
    # Passo a Passo:
        # Passo 1: Importar a Base de Dados
        # Passo 2: Visualizar a Base de Dados (2 Objetivos: Entender as Informações + Encontrar Problemas)
        # Passo 3: Resolver os Problemas da Base de Dados.
        # Passo 4: Análise Inicial ("Quantos Clientes Cancelaram?", "Qual a % (Porcentagem) de clientes?")
        # Passo 5: Analisar a Causa dos Cancelamentos dos Clientes.

# Usaremos o Pandas e o Plotly
    # Pandas -> Tratar Base de Dados
    # Plotly -> Criar Gráficos Dinâmicos

    # !pip install pandas openpyxl numpy nbformat plotly ipykernel
        # Por que instalar tudo isso?
            # Se colocasse "!pip install pandas plotly", o projeto ia funcionar para 90% dos computadores, 
            # mas por causa de algumas diferenças em certos computadores, é necessário colocar todos os
            # outros para que não haja problemas.

        # O que cada um pode fazer?
            # openpyxl -> Colabora com o Pandas para trabalhar com alguns tipos de Base de Dados.
            # numpy -> Colabora com o Pandas para fazer algumas operações.
            # nbformat -> Colabora com o Plotly para criar os gráficos.
            # ipykernel -> Colabora na exibição desses gráficos.

# Já que estamos no Notebook do Júpiter (.ipynb), nós podemos usa um "Print" mais bonito
    # Ou seja, ao invés de "print(tabela)", podemos usar o "display(tabela)"
    # Mostrará tudo de forma mais organizada e bonita, facilitando a visualização das informações.

    # Há também o "display(table.info())"
        # Esse formato ".info()", nos ajuda a detectar em qual formato cada coluna está (int, float ou object) 
        # e se há células/linhas/colunas vazias.

# Informações Inúteis
    # Elas tendem a te atrapalhar, às vezes deixando seu pc/programa pesado ou então não sendo úteis pro
    # que você precisa. Nesa forma você usa o ".drop()", que significa "tirar".
        # tabela = tabela.drop(columns="CustomerID")
    # Caso queira tirar mais de uma coluna em uma única vez, você vai fazer:
        # tabela = tabela.drop(columns=["CustomerID", "idade", "sexo"])
    
    # Caso haja campos vazios na sua Base de dados, você pode usar o .dropna()
        # tabela = tabela.dropna()
        # Assim ele te ajudará a ter um melhor resultado, sem os campos vazios te atrapalharem.
            # Obs: É importante destacar que só use o .dropna() caso sejam poucos campos vazios, ou
            # caso alguma coluna tenha muito campos sem dados, mas que não colaborarão muito com a
            # informação que você precisa.

        # Caso não possa jogar fora os campos vazios, você pode preenchê-los:
            # Manualmente;
            # Preenchendo todos os campos vazios com uma informação que você deseja;
                # tabela = tabela.fillna(0)
            # Preenchendo todos os campos vazios com a média de informação da coluna
                # tabela = tabela.fillna(mean("sexo"))
            # Preenchendo todos os campos vazios com a informação anterior a ele;
                # tabela = tabela.ffill()

# Analisando os Dados ("Quantos Clientes Cancelaram?", "Qual a % (Porcentagem) de clientes?")
    # Contar na coluna cancelou, quantos cancelaram e quantos não cancelaram.
        # display(tabela["cancelou"].value_counts())

    # Mostrar o valores em % (Percentual)
        # display(tabela["cancelou"].value_counts(normalize=True))