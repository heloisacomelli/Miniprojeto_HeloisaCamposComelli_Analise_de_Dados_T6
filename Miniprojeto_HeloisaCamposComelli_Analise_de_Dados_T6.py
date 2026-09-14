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

