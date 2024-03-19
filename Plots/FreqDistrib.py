#https://pt.stackoverflow.com/questions/270580/como-fazer-uma-tabela-de-distribui%C3%A7%C3%A3o-de-frequ%C3%AAncia-em-python

import pandas as pd
import matplotlib.pyplot as plt

# Supondo que você tenha uma base de dados em um arquivo CSV chamado 'dados.csv'
# Vamos carregar os dados usando pandas

names = ['ID','N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
output_file = '0-Datasets/cirrhosis2Clear.csv'
input_file = '0-Datasets/Cirrhosis2.csv'
dados = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ";",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que ? será considerado valores ausentes
# Vamos supor que você queira criar uma distribuição de frequência para uma coluna específica, por exemplo, 'idade'
coluna_alvo = 'Edema'

# Calcular a distribuição de frequência
distribuicao_freq = dados[coluna_alvo].value_counts().sort_index()

# Plotar a distribuição de frequência
plt.figure(figsize=(10, 6))
distribuicao_freq.plot(kind='bar')
plt.title('Distribuição de Frequência de {}'.format(coluna_alvo))
plt.xlabel(coluna_alvo)
plt.ylabel('Frequência')
plt.grid(axis='y')
plt.show()