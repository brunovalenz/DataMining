import numpy as np
from sklearn.mixture import GaussianMixture
import pandas as pd
import matplotlib.pyplot as plt

# Dados normalizados

names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
X = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes

# Criando o modelo GMM
gmm = GaussianMixture(n_components=3)  # Defina o número de componentes desejado

# Treinando o modelo
gmm.fit(X)

# Prevendo as classes dos dados
labels = gmm.predict(X)

# Obtendo as probabilidades de pertencimento a cada classe
probs = gmm.predict_proba(X)

# Plotando os resultados
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.colorbar()
plt.show()