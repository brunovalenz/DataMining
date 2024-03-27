import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
dados = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes

# Criar o boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(dados['Age'])

# Adicionar título e rótulos aos eixos
plt.title('Boxplot')
plt.ylabel('Valores')

# Mostrar o boxplot
plt.grid(True)
plt.show()