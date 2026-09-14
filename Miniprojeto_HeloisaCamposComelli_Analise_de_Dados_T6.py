# Importando a biblioteca pandas
import pandas as pd

# Lendo o arquivo CSV com a indicação do separador brasileiro utilizado e da codificação
df = pd.read_csv("Base Varejo.csv", sep=";", encoding="utf-8")

#Inspecionando o arquivo CSV
print(f"Dimensões do data frame: {df.shape}") # Verificando o número de linhas e colunas do data frame

print(f"Colunas: {list(df.columns)}") # Verificando os nomes das colunas

df.info() # Verificando o tipo de cada dado do data frame na forma de uma tabela

print(f"Quantidade de valores nulos em cada coluna: \n{df.isnull().sum()}") # Confirmando que só existem valores nulos nas colunas vazias identificadas como "Unnamed: " pelo Pandas"
print(f"Primeiras linhas do data frame: \n{df.head()}") # Mostrando as cinco primeiras linhas do data frame

# Verificando a presença de linhas duplicadas no data frame 
print(f"Quantidade de linhas duplicadas: {df.duplicated().sum()}") # Contabilizando a quantidade de linhas duplicadas
print(f"Linhas duplicadas: \n{df[df.duplicated(keep=False)].sort_values(by=df.columns.tolist())}") # Visualizando as linhas duplicadas do data frame de forma odenada

# Verificando a presença de categorias vazias identidicadas como "#N/D" no data frame
print(f"Quantidade de campos identificados como #N/D: \n{df[df == '#N/D'].count()}") # Contabilizando a quantidade de categorias vazias 
print(f"Linhas com campos preenchidos com '#N/D': \n{df[(df == '#N/D').any(axis=1)]}") # Visualizando as linhas com campos preenchidos com "#N/D" no data frame

nome_nulo = df[df['PR_NOME'] == '#N/D'] # Criando um data frame com os produtos que não possuem nome
categoria_nula = df[df['PR_CAT'] == '#N/D'] # Criando um data frame com os produtos que não possuem categoria

print(f"Códigos dos produtos sem nome: \n{nome_nulo.groupby('PR_NOME')['PR_ID'].unique()}") # Visualizando o código o nomeados como "#N/D" para vefiricar se existe um nome de produto vinculado ao ID 107
print(f"Códigos dos produtos sem categoria: \n{categoria_nula.groupby('PR_CAT')['PR_ID'].unique()}")

ID_107 = df[df['PR_ID'] == 107] # Criando um data frame com o produto que possui o ID 107
print(f"Nomes e categorias relacionados ao ID 107: \n{ID_107[['PR_NOME', 'PR_CAT']].drop_duplicates()}") # Visualizando os nomes e categorias do produto com ID 107

# Verificando a falta de padronização de textos nas colunas CL_GENERO, PR_CAT e PR_NOME
print(f"Dados da coluna CL_GENERO: \n{df['CL_GENERO'].unique()}") # Visualizando os dados da coluna CL_GENERO para verificar a falta de padronização de textos
print(f"Dados da coluna PR_CAT: \n{df['PR_CAT'].unique()}") # Visualizando os dados da coluna PR_CAT para verificar a falta de padronização de textos
print(f"Dados da coluna PR_NOME: \n{df['PR_NOME'].unique()}") # Visualizando os dados da coluna PR_NOME para verificar a falta de padronização de textos

# Realizando o tratamento de strings e datas
df = df.map(lambda x: x.strip().upper() if isinstance(x, str) else x) # Retirando possíveis espaços em branco no início e no final das strings e padronizando todas as letras para maiúsculas
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce') # Convertendo a coluna 'DATA' para o formato de data. errors= 'coerce' foi utilizado para converter possíveis erros em NaT
print(f"Valores nulos na coluna 'DATA' após a conversão: {df['DATA'].isnull().sum()}") # Verificando possíveis erros que geraram dados nulos na coluna 'DATA' após a conversão
print(f"Primeiras linhas do data frame após o tratamento de strings e datas: \n{df.head()}") # Visualizando as cinco primeiras linhas do data frame após o tratamento de strings e datas
print(f"Tipo dos dados de cada coluna após o tratamento de strings e datas: \n{df.dtypes}") # Verificando o tipo de cada dado do data frame após o tratamento de strings e datas

# Substituindo os campos identificados como "#N/D" para facilitar a análise de dados
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'SEM CATEGORIA') # Substituindo os campos identificados como "#N/D" na coluna PR_CAT para "SEM CATEGORIA"
df['PR_NOME'] = df['PR_NOME'].replace('#N/D', 'SEM NOME') # Substituindo os campos identificados como "#N/D" na coluna PR_NOME para "SEM NOME"

# Realizando a limpeza das colunas nulas identificadas como "Unnamed " pelo Pandas
df = df.dropna(axis=1, how='all') # Removendo as colunas que possuem todos os valores nulos
print(f"Dimensões do data frame após a limpeza das colunas nulas: {df.shape}") # Verificando o número de linhas e colunas do data frame após a limpeza das colunas nulas

# Realizando a exclusão de linhas duplicadas com o mesmo CO_ID, mantendo apenas a primeira ocorrência
print(f"Contagem de linhas dup'licadas com o mesmo CO_ID: \n{df[df.duplicated(keep=False)]['CO_ID'].value_counts()}") # Verificando a ocorrência de linhas duplicadas dentro de uma mesma compra
df = df.drop_duplicates() # Removendo as linhas referentes ao mesmo CO_ID que apresentam informações duplicadas
print(f"Dimensões do data frame após a exclusão de linhas duplicadas com o mesmo CO_ID: {df.shape}") # Verificando o número de linhas e colunas do data frame após a exclusão de linhas duplicadas com o mesmo CO_ID

# Gerando estatísticas básicas para a coluna CL_FHL
print(f"Estatísticas básicas da coluna CL_FHL: \n{df['CL_FHL'].describe()}") # Gerando estatísticas básicas para a coluna CL_FHL
print(f"Moda da coluna CL_FHL: {df['CL_FHL'].mode()[0]}") # Verificando a moda da coluna CL_FHL

# Avaliando a relação entre o gênero, segmentação econômica do cliente e o número de compras realizadas
classe_compras = df.pivot_table(
    index='CL_GENERO',
    columns= 'CL_SEG',
    values='CO_ID',
    aggfunc='nunique'
)
print(f"Relação entre o gênero e segmentação econômica do cliente e o número de compras realizadas: \n{classe_compras}") 

# Avaliando os produtos mais vendidos
dez_mais_vendidos = df.groupby('PR_NOME').size().sort_values(ascending=False).head(10)
print(f"Produtos mais vendidos: \n{dez_mais_vendidos}") # Visualizando os 10 produtos mais vendidos

# Verificando as categorias mais vendidas por gênero dos clientes
genero_produto = df.pivot_table(
    index='CL_GENERO',
    columns='PR_CAT',
    values='CO_ID',
    aggfunc='count',
    fill_value=0
)
print(f"Categorias mais vendidas por gênero dos clientes: \n{genero_produto}") # Visualizando as categorias mais vendidas por gênero dos clientes
