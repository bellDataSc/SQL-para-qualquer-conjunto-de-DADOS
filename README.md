# SQL para Análise de Dados Orçamentários no Governo de São Paulo

Por Isabel Gonçalves Cruz

**Atualizações**: Add os cod atreves do notebook do **Google Colab** em XML no banco de dados Oracle.

                  **Transformando as consultas** XML em **SQL**

## Este repositório documenta e disponibiliza scripts SQL e XML
utilizados na análise de dados orçamentários e financeiros do Governo do Estado de São Paulo. O foco é a manipulação e extração de dados do SIGEO (Sistema de Informações Gerenciais da Execução Orçamentária), um banco de dados que viabiliza a gestão e transparência dos gastos públicos através de consultas SQL e geração de relatórios.

## Ferramentas utilizadas: 
Oracle Business Intelligence, PostgreSQL, Pandas, Power BI

## Objetivo: 
Facilitar a extração e análise de dados orçamentários para embasar decisões estratégicas na gestão pública

Banco Oracle Business Intelligence


  **Comandos utilizados como Analista de Dados Técnica PL pelo Governo de Estado de São Paulo [Nov/2024 - até o momento] 
  **OBS: JANEIRO de 2025/ add buscas utilizadas de SQL e XML no **SIGEO** (SIGEO: Sistema de Informações Gerenciais da Execução Orçamentária) praticamente o banco de dados da União que possibilita a gestão e transparência dos gastos públicos, através da elaboração de consultas e relatórios. 
  **Quando criei o repositório estava em exercio pelo Estado de Minas Gerais, tambem como Analista de Dados PL, ambos os governos de estado MG e SP usam do mesmo sistema.


 ## 🗂 Estrutura do Repositório

- queries/: Contém consultas SQL para extração de dados

- notebooks/: Notebooks Jupyter com análises exploratórias

- datasets/: Conjuntos de dados simulados para testes

- docs/: Documentação detalhada sobre cada consulta e metodologia

## 🔍 Principais Análises Realizadas
## 1️⃣ Importação e Conexão ao Banco de Dados

O primeiro passo para a análise de dados é estabelecer a conexão com o banco de dados do SIGEO.

Banco: Oracle Business Intelligence


## 2️⃣ Limpeza e Tratamento de Dados

Inspeção inicial: Visualização das primeiras linhas e verificação de valores ausentes

Tratamento de valores nulos: Substituição por média ou remoção conforme necessidade

Remoção de duplicatas: Garantia da integridade dos dados

Conversão de tipos: Ajustes para facilitar análises e visualizações

Criação de colunas derivadas: Classificação de indicadore

## 3️⃣ Extração de Indicadores Chave

Consultas para obtenção de informações relevantes, como:

Execução orçamentária por órgão

Comparativo entre dotação inicial e executada

Distribuição de empenhos e pagamentos por região e setor

Identificação de padrões e anomalias nos gastos

## 4️⃣ Visualização e Geração de Relatórios

Os dados tratados e agregados são exportados para o Power BI, permitindo dashboards interativos para acompanhamento da execução orçamentária.

## 📂 Exemplos de Código

Consulta SQL para verificar os valores empenhados por órgão:

  SELECT orgao, SUM(valor_empenhado) AS total_empenhado
FROM execucao_orcamentaria
WHERE ano = 2024
GROUP BY orgao
ORDER BY total_empenhado DESC;

## Carregamento dos dados no Pandas:

from sqlalchemy import create_engine
import pandas as pd

 //Conectar ao banco de dados
engine = create_engine('postgresql://usuario:senha@host:porta/database')
query = """
SELECT * FROM execucao_orcamentaria WHERE ano = 2024;
"""
df = pd.read_sql(query, engine)


📧 Contato

Para dúvidas ou colaborações, entre em contato pelo LinkedIn ou via e-mail.

📌 Autor: Bel - Analista de Dados Técnica PL - Governo do Estado de São Paulo





