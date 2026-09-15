# Miniprojeto – Análise de Dados com Python

## 1. Sobre o projeto

Este projeto foi desenvolvido como atividade do curso **Análise de Dados com Python [T6]**, com o objetivo de aplicar técnicas de **Análise Exploratória de Dados (AED)** utilizando Python e a biblioteca pandas.

A análise foi realizada sobre uma base de dados de varejo, contendo informações sobre compras, clientes e produtos. O trabalho contempla a inspeção da qualidade dos dados, tratamento de inconsistências, remoção de duplicidades, conversão de tipos, estatísticas descritivas e agrupamentos para identificação de padrões.

O objetivo principal é transformar uma base de dados bruta em uma base tratada e gerar informações que possam auxiliar na compreensão do comportamento das compras.

---

## 2. Estrutura da base de dados

A base original possui informações relacionadas a:

| Coluna      | Descrição                             |
| ----------- | ------------------------------------- |
| `DATA`      | Data da compra                        |
| `CO_ID`     | Número da compra/nota fiscal          |
| `CL_ID`     | Identificação do cliente              |
| `CL_GENERO` | Sexo biológico informado pelo cliente |
| `CL_EC`     | Estado civil do cliente               |
| `CL_FHL`    | Quantidade de filhos                  |
| `CL_SEG`    | Segmento econômico do cliente         |
| `PR_ID`     | Código/SKU do produto                 |
| `PR_CAT`    | Categoria do produto                  |
| `PR_NOME`   | Nome do produto                       |

A regra de negócio considerada na análise é que **cada linha representa um item comprado**. Por esse motivo, o mesmo `CO_ID` pode aparecer em várias linhas, representando diferentes itens pertencentes a uma mesma compra.

---

## 3. Tecnologias utilizadas

* Python
* Pandas
* Visual Studio Code ou Google Colab
* Git e GitHub

---

## 4. Importação e inspeção inicial

A base foi carregada utilizando pandas:

```python
df = pd.read_csv("Base Varejo.csv", sep=";", encoding="utf-8")
```

Inicialmente, a base apresentava:

* **830.000 registros**
* **14 colunas**
* 10 colunas relacionadas aos dados da análise
* 4 colunas completamente vazias (`Unnamed: 10` até `Unnamed: 13`)

Também foram analisados os tipos de dados, valores nulos, linhas duplicadas e ocorrências de `#N/D`.

---

## 5. Problemas identificados na base

Durante a análise inicial foram identificados os seguintes problemas de qualidade:

### 5.1 Colunas completamente vazias

As colunas:

* `Unnamed: 10`
* `Unnamed: 11`
* `Unnamed: 12`
* `Unnamed: 13`

possuíam **830.000 valores nulos cada**, não apresentando informações úteis para a análise.

Essas colunas foram removidas.

### 5.2 Valores `#N/D`

Foram identificadas **3.650 ocorrências de `#N/D` em `PR_CAT`** e **3.650 ocorrências em `PR_NOME`**.

Todas essas ocorrências estavam relacionadas ao produto de código `PR_ID = 107`.

Como não havia informações suficientes para descobrir a categoria ou o nome correto desse produto, os valores foram substituídos por:

* `#N/D` → `SEM CATEGORIA`
* `#N/D` → `SEM NOME`

Dessa forma, a informação não foi simplesmente apagada e a existência do dado desconhecido foi preservada.

### 5.3 Datas

A coluna `DATA` originalmente estava armazenada como texto.

Ela foi convertida para o tipo `datetime` utilizando o formato brasileiro:

```python
df['DATA'] = pd.to_datetime(
    df['DATA'],
    format='%d/%m/%Y',
    errors='coerce'
)
```

Após a conversão, não foram encontrados valores nulos resultantes de datas inválidas.

### 5.4 Duplicidades

Inicialmente foram identificadas **96.553 linhas completamente duplicadas**.

É importante destacar que **não foram excluídas todas as linhas que possuíam o mesmo `CO_ID`**.

Isso ocorre porque, de acordo com a regra de negócio da base, cada linha representa um item comprado. Portanto, um mesmo `CO_ID` pode aparecer várias vezes legitimamente quando uma compra contém vários produtos.

Como não havia informação suficiente para determinar se registros aparentemente iguais pertencentes ao mesmo `CO_ID` representavam unidades diferentes de um produto ou registros duplicados, foi adotada uma abordagem conservadora:

> **Foram removidas somente as linhas completamente idênticas em todas as colunas.**

A remoção foi realizada com:

```python
df = df.drop_duplicates()
```

Essa decisão evita eliminar possíveis registros legítimos apenas por possuírem o mesmo número de compra.

Após a remoção das duplicidades completas, a base passou de **830.000 para 733.447 registros**.

---

## 6. Padronização dos dados

As informações textuais foram padronizadas para remover espaços desnecessários e uniformizar as letras:

```python
df = df.map(
    lambda x: x.strip().upper()
    if isinstance(x, str) else x
)
```

Também foram realizadas as seguintes transformações:

* conversão de `DATA` para `datetime`;
* substituição de `#N/D` por `SEM CATEGORIA` e `SEM NOME`;
* remoção das colunas completamente nulas;
* remoção das linhas completamente duplicadas.

Após o tratamento, a base passou a apresentar:

* **733.447 registros**
* **10 colunas**
* **0 valores nulos**
* **0 linhas completamente duplicadas**

---

## 7. Estatísticas descritivas – número de filhos

Foi realizada uma análise estatística da coluna `CL_FHL`, correspondente à quantidade de filhos dos clientes.

| Estatística             | Resultado |
| ----------------------- | --------: |
| Quantidade de registros |   733.447 |
| Média                   |      1,15 |
| Mediana                 |         0 |
| Moda                    |         0 |
| Desvio padrão           |      1,42 |
| Mínimo                  |         0 |
| Máximo                  |         4 |
| 1º quartil              |         0 |
| 2º quartil              |         0 |
| 3º quartil              |         2 |

Os resultados indicam que a quantidade de filhos apresenta concentração em valores baixos. Tanto a mediana quanto a moda são iguais a zero.

---

## 8. Agrupamentos e análises

Foram realizadas diferentes análises utilizando `groupby()` e `pivot_table()`.

### 8.1 Compras por gênero e segmento econômico

Foi analisada a quantidade de compras distintas (`CO_ID`) por gênero e segmento econômico.

| Gênero | Segmento A | Segmento B | Segmento C |
| ------ | ---------: | ---------: | ---------: |
| F      |        700 |      5.946 |      2.969 |
| M      |        792 |      5.897 |      2.167 |

O segmento **B apresenta a maior quantidade de compras distintas para os dois gêneros**.

### 8.2 Produtos com maior quantidade de registros

Os dez produtos com maior quantidade de registros foram:

| Produto            | Registros |
| ------------------ | --------: |
| PRESUNTO COZIDO    |    12.719 |
| SARDINHA           |     6.610 |
| BANANA             |     6.518 |
| ESCOVA DE DENTE    |     6.518 |
| GEL                |     6.517 |
| PAPINHA INFANTIL   |     6.515 |
| MODELADOR          |     6.505 |
| CERA               |     6.502 |
| CEBOLA             |     6.501 |
| LIMPADOR PERFUMADO |     6.501 |

Nesse agrupamento, a quantidade representa **registros de itens na base**, e não necessariamente o número de compras distintas.

### 8.3 Categorias por gênero

Também foi analisada a quantidade de registros de produtos por gênero e categoria.

| Gênero | Acessórios | Alimentos | Bebidas | Higiene | Limpeza |    Pet | Sem Categoria |
| ------ | ---------: | --------: | ------: | ------: | ------: | -----: | ------------: |
| F      |      6.839 |   200.274 |  19.764 |  71.721 |  67.328 | 14.809 |         1.692 |
| M      |      6.032 |   183.923 |  18.500 |  65.981 |  61.304 | 13.744 |         1.536 |

A categoria **ALIMENTOS** apresenta a maior quantidade de registros para ambos os gêneros.

---

## 9. Resultado final da base

Após o tratamento, foram obtidos os seguintes resultados:

| Indicador                       | Resultado |
| ------------------------------- | --------: |
| Registros                       |   733.447 |
| Colunas                         |        10 |
| Produtos distintos              |       229 |
| Compras distintas               |    18.471 |
| Clientes distintos              |     1.000 |
| Valores nulos                   |         0 |
| Linhas completamente duplicadas |         0 |

A base tratada foi exportada para o arquivo:

**`Base Varejo Tratada.csv`**

---

## 10. Principais insights

A análise exploratória permitiu identificar os seguintes pontos:

1. **O segmento econômico B concentra a maior quantidade de compras distintas**, tanto entre clientes do gênero feminino quanto do masculino.

2. **A categoria ALIMENTOS possui a maior quantidade de registros de itens**, sendo a categoria mais frequente para ambos os gêneros.

3. **PRESUNTO COZIDO é o produto com maior quantidade de registros na base tratada**, com 12.719 ocorrências.

4. **A quantidade de filhos dos clientes está concentrada em valores baixos**: a média é de 1,15 filho, enquanto a mediana e a moda são iguais a zero.

5. **A remoção de duplicidades reduziu a base de 830.000 para 733.447 registros**, porém somente linhas completamente idênticas foram removidas. Registros com o mesmo `CO_ID` não foram automaticamente considerados duplicados.

6. **O produto de código 107 permanece sem nome e categoria identificados**, sendo representado na base tratada por `SEM NOME` e `SEM CATEGORIA`.

---

## 11. Reflexão sobre ETL e qualidade dos dados

O processo realizado neste projeto pode ser relacionado às três etapas do conceito de **ETL (Extract, Transform, Load)**.

### Extract – Extração

A etapa de extração correspondeu à leitura do arquivo `Base Varejo.csv` utilizando pandas. Nesse momento, foram verificadas as dimensões da base, suas colunas e os tipos de dados.

### Transform – Transformação

A maior parte do trabalho ocorreu nessa etapa. Foram identificados e tratados problemas de qualidade, como:

* colunas completamente vazias;
* valores `#N/D`;
* dados textuais com necessidade de padronização;
* datas armazenadas como texto;
* registros completamente duplicados.

Também foram realizadas análises exploratórias por meio de estatísticas descritivas e agrupamentos.

A decisão de não remover registros apenas porque possuíam o mesmo `CO_ID` foi importante para respeitar a regra de negócio da base. Como cada linha representa um item comprado, várias linhas com o mesmo `CO_ID` podem representar uma única compra contendo vários produtos.

### Load – Carregamento

Depois do tratamento, a base foi exportada novamente para um arquivo CSV:

**`Base Varejo Tratada.csv`**

Esse arquivo pode ser utilizado posteriormente em novas análises sem a necessidade de repetir as etapas básicas de limpeza.

---

## 12. Possíveis limitações

Apesar do tratamento realizado, algumas questões permanecem:

* Não foi possível identificar o nome e a categoria corretos do produto `PR_ID = 107`.
* Não é possível determinar, somente com os dados disponíveis, se todos os registros com o mesmo produto e `CO_ID` representam unidades distintas ou alguma duplicidade não identificada.
* As análises de produtos e categorias foram realizadas sobre a quantidade de registros de itens, não sobre a quantidade de compras distintas.
* A base não contém informações suficientes para aprofundar determinadas análises sobre o comportamento individual dos clientes.

---

## 13. Como executar

Para executar o projeto localmente, é necessário ter Python e pandas instalados.

Com os arquivos na mesma pasta, execute:

```bash
python Miniprojeto_HeloisaCamposComelli_Analise_de_Dados_T6.py
```

O script realizará a leitura da base original, fará o tratamento dos dados, exibirá os resultados das análises e criará o arquivo:

```text
Base Varejo Tratada.csv
```

---

## 14. Arquivos do projeto

A estrutura esperada do repositório é:

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

## 15. Conclusão

O projeto permitiu aplicar conceitos de análise exploratória, tratamento de dados e qualidade de dados utilizando Python e pandas.

A partir da base original, foram identificados problemas de estrutura, valores ausentes, inconsistências representadas por `#N/D`, tipos de dados inadequados e duplicidades. Após o tratamento, foi obtida uma base mais adequada para análises posteriores.

Além da limpeza, os agrupamentos realizados possibilitaram identificar padrões relacionados a gênero, segmento econômico, categorias e produtos, contribuindo para uma visão inicial do comportamento das compras na base de varejo.