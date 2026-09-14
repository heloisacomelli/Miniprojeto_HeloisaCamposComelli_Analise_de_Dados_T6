# Importando a biblioteca pandas
import pandas as pd

# Lendo o arquivo CSV com a indicação do separador brasileiro utilizado e da codificação
df = pd.read_csv("Base Varejo.csv", sep=";", encoding="utf-8")

#Inspecionando o arquivo CSV
print(f"Dimensões do data frame: {df.shape}") # Verificando o número de linhas e colunas do data frame
print(f"Colunas: {list(df.columns)}") # Verificando os nomes das colunas
df.info() # Verificando o tipo de cada dado do data frame na forma de uma tabela
print(f"Quantidade de valores nulos em cada coluna: \n{df.isnull().sum()}") # Confirmando que só existem valores nulos nas colunas vazias identificadas como "Unnamed: " pelo Pandas"
print(f"Visualizando as primeiras linhas do data frame: \n{df.head()}") # Mostrando as cinco primeiras linhas do data frame
