import matplotlib.pyplot as plt
import pandas as pd

# Sample data



names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
dados = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes
dadoX = 'Age'
dadoY = 'Cholesterol'

x = dados[dadoX]
y = dados[dadoY]

# Create scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Show the plot
plt.show()