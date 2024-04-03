import pandas as pd
import matplotlib.pyplot as plt

# Definindo as informações fornecidas
names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
features = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'

# Carregando os dados
dados = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Calcular a matriz de covariância
covariance_matrix = dados.cov()

# Visualizar a matriz de covariância
plt.figure(figsize=(10, 8))
plt.imshow(covariance_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Covariance')
plt.xticks(ticks=range(len(features)), labels=features, rotation=90)
plt.yticks(ticks=range(len(features)), labels=features)
plt.title('Matriz de Covariância')
plt.show()
