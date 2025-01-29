
  ## SQL para analizar qualquer conjunto de DADOS

  Comandos utilizados como Analista de Dados Técnica PL pelo Governo de Estado de São Paulo [Nov/2024 - até o momento]
  OBS: JANEIRO de 2025/ add buscas utilizadas de SQL no **SIGEO** (SIGEO: Sistema de Informações Gerenciais da Execução Orçamentária) praticamente o banco de dados da União que possibilita a gestão e transparência dos gastos públicos, através da elaboração de consultas e relatórios. 
  - Banco Oracle Business Intelligence

  ## 1 - Importando Conjuntos de Dados

Como parte do meu trabalho como analista de dados, desenvolvi vários projetos que envolvem a importação e análise de conjuntos de dados. Para executar consultas SQL, precisamos importar os conjuntos de dados relevantes. Recomendo fortemente que baixe o arquivo Excel disponível em {conjunto de dados.xlsx} que contém o esquema e os dados bem similar ao que eu utilizo no meu trabalho com análises. 

  # Explicação do Código:
  
  1.1 Conectando ao Banco de Dados: Usamos create_engine para conectar ao PostgreSQL.
  
  2. Carregando os Dados: Utilizamos pd.read_sql para carregar os dados da tabela 'indicadores'.
  
  3. Inspeção Inicial: Exibimos as primeiras linhas do dataframe e verificamos a presença de valores nulos.
  
  4. Tratamento de Valores Nulos: Substituímos valores nulos na coluna 'valor' pela média e removemos linhas com valores nulos nas colunas 'indicador_nome' e 'data'.
  
  5. Remoção de Duplicatas: Eliminamos registros duplicados.
  
  6. Conversão de Tipos de Dados: Convertendo a coluna 'data' para o tipo datetime.
  
  7. Criação de Nova Coluna: Adicionamos uma coluna 'categoria' para categorizar os valores dos indicadores.
 
  8. Salvando os Dados Limpos: Gravamos o dataframe limpo de volta no banco de dados em uma nova tabela 'indicadores_limpos'.
