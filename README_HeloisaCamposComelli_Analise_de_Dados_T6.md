# Instruções de Execução – Miniprojeto Análise de Dados com Python

## 1. Sobre o projeto

Este arquivo contém as instruções básicas para executar o miniprojeto desenvolvido para o curso **Análise de Dados com Python [T6]**.

O projeto utiliza Python e pandas para realizar a análise exploratória e o tratamento de uma base de dados de varejo.

---

## 2. Arquivos necessários

Para executar o projeto, os seguintes arquivos devem estar disponíveis no mesmo diretório:

```text
Base Varejo.csv
Miniprojeto_HeloisaCamposComelli_Analise_de_Dados_T6.py
```

O arquivo `Base Varejo Tratada.csv` será gerado automaticamente pelo script após a execução.

---

## 3. Requisitos

É necessário ter instalado:

* Python 3;
* biblioteca pandas.

Caso o pandas ainda não esteja instalado, utilize:

```bash
pip install pandas
```

---

## 4. Execução no Visual Studio Code

### Passo 1 – Abrir o projeto

Abra a pasta do projeto no Visual Studio Code.

### Passo 2 – Conferir os arquivos

Verifique se o arquivo Python e a base original estão na mesma pasta:

```text
Base Varejo.csv
Miniprojeto_HeloisaCamposComelli_Analise_de_Dados_T6.py
```

### Passo 3 – Executar o script

Abra o terminal do Visual Studio Code e execute:

```bash
python Miniprojeto_HeloisaCamposComelli_Analise_de_Dados_T6.py
```

Caso o ambiente utilize o comando `python3`, execute:

```bash
python3 Miniprojeto_HeloisaCamposComelli_Analise_de_Dados_T6.py
```

---

## 5. Execução no Google Colab

Também é possível executar o projeto no Google Colab.

1. Acesse o Google Colab.
2. Crie um novo notebook.
3. Faça o upload do arquivo Python.
4. Faça o upload do arquivo `Base Varejo.csv`.
5. Execute o código.

Caso seja necessário instalar o pandas no ambiente:

```python
!pip install pandas
```

---

## 6. O que o script realiza

Ao ser executado, o script:

1. Importa a biblioteca pandas.
2. Carrega a base `Base Varejo.csv`.
3. Exibe as dimensões, colunas e tipos de dados.
4. Verifica valores nulos.
5. Identifica linhas completamente duplicadas.
6. Identifica ocorrências de `#N/D`.
7. Verifica os produtos relacionados ao código `PR_ID = 107`.
8. Padroniza os dados textuais.
9. Converte a coluna `DATA` para o tipo `datetime`.
10. Substitui `#N/D` por `SEM CATEGORIA` e `SEM NOME`.
11. Remove colunas completamente vazias.
12. Remove somente linhas completamente duplicadas.
13. Calcula estatísticas descritivas da coluna `CL_FHL`.
14. Realiza agrupamentos por gênero e segmento econômico.
15. Identifica os produtos com maior quantidade de registros.
16. Analisa as categorias de produtos por gênero.
17. Exibe um relatório final.
18. Salva a base tratada como `Base Varejo Tratada.csv`.

---

## 7. Observação sobre os registros duplicados

O script considera que cada linha da base representa um **item comprado**.

Por esse motivo, o fato de o mesmo `CO_ID` aparecer em várias linhas não significa, por si só, que os registros sejam duplicados.

Uma mesma compra pode conter vários produtos e, consequentemente, possuir várias linhas com o mesmo `CO_ID`.

Como não havia informação suficiente para determinar se registros idênticos dentro de uma mesma compra representavam unidades diferentes de um produto ou registros duplicados, foi adotado um tratamento conservador:

```python
df = df.drop_duplicates()
```

Assim, foram removidas **somente as linhas completamente idênticas em todas as colunas**, sem eliminar automaticamente todas as linhas que compartilham o mesmo `CO_ID`.

---

## 8. Arquivo gerado

Após a execução, será criado:

```text
Base Varejo Tratada.csv
```

A base tratada possui:

* **733.447 registros**
* **10 colunas**
* **0 valores nulos**
* **0 linhas completamente duplicadas**

O arquivo pode ser utilizado para análises posteriores.

---

## 9. Estrutura final esperada

```text
Miniprojeto_HeloisaCamposComelli_Analise_de_Dados_T6/
│
├── README.md
├── README_HeloisaCamposComelli_Analise_de_Dados_T6.md
├── Miniprojeto_HeloisaCamposComelli_Analise_de_Dados_T6.py
├── Base Varejo.csv
└── Base Varejo Tratada.csv
```

---

## 10. Observação

Para conhecer a metodologia utilizada, os resultados das análises, os principais insights e a reflexão sobre ETL e qualidade dos dados, consulte o arquivo **`README.md`** deste repositório.