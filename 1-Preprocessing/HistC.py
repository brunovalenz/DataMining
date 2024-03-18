import pandas as pd
import matplotlib.pyplot as plt

names = ['ID','N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/Cirrhosis2.csv'
dados = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ";",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes

# Plotar o histograma
choice = 'Drug'
plt.hist(dados[choice], bins=10, color='skyblue', edgecolor='black')

# Adicionar título e rótulos aos eixos
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')

# Mostrar o histograma
plt.show()