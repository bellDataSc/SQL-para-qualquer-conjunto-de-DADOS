# Alinhamento das minhas imformações, importação de dados, estrutura para definir media de valores.

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive
drive.mount('/content/drive', force_remount=True)
base_path = "/content/drive/Mydrive/1st_phase-selective-process-data-science-dataBase.csv/"

#Panorama 
ny.info()
ttn.info()

#Sumário estatistico de features numéricas do dataset com número máximos, mínimo, média, desvio padrão, quartis e contaem de valores em cada coluna.
ttn.describe()
ttn.describe().round(2)


#Lendo cada variavel, imprindo media definida

df_salario_mensal = pd.read_csv(path_to_data + '1st_phase-selective-process-data-science-dataBase.csv')
print (df_salario_mensal.shape)
df_salario_mensal.sample(5)

df_local = pd.read_csv('1st_phase-selective-process-data-science-dataBase.csv')
print (df_local.shape)
df_local.head()


#Armazenando o valor desejado em uma variável
salario = ttn[ttn['salario'] == 1][ttn['local'] == 'salario']['local'].median())
#Selecionar a coluna que vai receber os valores e especificar as condições = 
coluna.fillna(variável)
ttn['local'][ttn['Salario'] == 1][ttn['Salario'] == 'x'] = ttn['local'].fillna(lo_sa_median);



