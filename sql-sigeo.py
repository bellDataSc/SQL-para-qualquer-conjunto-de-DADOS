import pandas as pd 

\\Criando um DataFrame com os valores de Empenhado, Liquidado e Pago para 2023 e 2024

df_fluxo_documentos_2024 = pd.read_csv("Fluxo Documentos 2024.xlsx - Sheet1.csv", header=1) 

\\Filtrar o DataFrame para 2023 e 2024

df_fluxo_documentos_2023 = df_fluxo_documentos_2024[ df_fluxo_documentos_2024["Ano Referência"] == 2023 ] df_fluxo_documentos_2024 = df_fluxo_documentos_2024[ df_fluxo_documentos_2024["Ano Referência"] == 2024 ] 

\\Criando um dicionário com os valores de Empenhado, Liquidado e Pago para 2023 e 2024

data = { "Ano": [2023, 2024], "Empenhado": [ df_fluxo_documentos_2023["Empenhado"].sum(), df_fluxo_documentos_2024["Empenhado"].sum(), ], 
        "Liquidado": [ df_fluxo_documentos_2023["Liquidado"].sum(), df_fluxo_documentos_2024["Liquidado"].sum(), ], 
        "Pago": [ df_fluxo_documentos_2023["Pago"].sum(), df_fluxo_documentos_2024["Pago"].sum(), ], } 

