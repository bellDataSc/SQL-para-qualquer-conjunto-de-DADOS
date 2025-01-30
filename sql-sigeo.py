import pandas as pd 

\\Criando um DataFrame com os valores de Empenhado, Liquidado e Pago para 2023 e 2024

df_fluxo_documentos_2024 = pd.read_csv("Fluxo Documentos 2024.xlsx - Sheet1.csv", header=1) 

\\Filtrar o DataFrame para 2023 e 2024

df_fluxo_documentos_2023 = df_fluxo_documentos_2024[ df_fluxo_documentos_2024["Ano Referência"] == 2023 ] df_fluxo_documentos_2024 = df_fluxo_documentos_2024[ df_fluxo_documentos_2024["Ano Referência"] == 2024 ] 

\\Criando um dicionário com os valores de Empenhado, Liquidado e Pago para 2023 e 2024

data = { "Ano": [2023, 2024], "Empenhado": [ df_fluxo_documentos_2023["Empenhado"].sum(), df_fluxo_documentos_2024["Empenhado"].sum(), ], 
        "Liquidado": [ df_fluxo_documentos_2023["Liquidado"].sum(), df_fluxo_documentos_2024["Liquidado"].sum(), ], 
        "Pago": [ df_fluxo_documentos_2023["Pago"].sum(), df_fluxo_documentos_2024["Pago"].sum(), ], } 

\\Criando um DataFrame a partir do dicionário

df = pd.DataFrame(data) 

\\Criando uma tabela dinâmica com Ano como linhas e Empenhado, Liquidado e Pago como colunas

df_pivot = df.pivot_table( index=["Ano"], values=["Empenhado", "Liquidado", "Pago"], aggfunc="sum" ) 

\\Exibir as primeiras 5 linhas da tabela dinâmica

print("First 5 rows of Pivot:") print(df_pivot.head().to_markdown(index=False, numalign="left", stralign="left")) 

\\Exibir os nomes das colunas e seus tipos de dados

print("\nData Types:") print(df_pivot.info()) 

