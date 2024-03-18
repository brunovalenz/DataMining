import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo (substitua isso pelos seus próprios dados)
names = ['ID','N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
output_file = '0-Datasets/cirrhosis2Clear.csv'
input_file = '0-Datasets/Cirrhosis2.csv'
dados = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ";",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='?')      # Define que ? será considerado valores ausentes

# Plotar o histograma
choices = ['Age', 'Drug', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
plt.hist(choices, bins=10, color='skyblue', edgecolor='black')

# Adicionar título e rótulos aos eixos
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')

# Mostrar o histograma
plt.show()