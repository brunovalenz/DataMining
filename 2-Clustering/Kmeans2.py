import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
data = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes
# Carregar os dados
#data = np.loadtxt('/c:/Users/bruno/Desktop/bu/arquivos/python/DataMining/0-Datasets/cirrhosis2Clear.csv')

# Definir o número de clusters desejado
k = 3

# Criar o objeto KMeans
kmeans = KMeans(n_clusters=k)

# Treinar o modelo
kmeans.fit(data)

# Obter os rótulos dos clusters
labels = kmeans.labels_

# Obter as coordenadas dos centróides
centroids = kmeans.cluster_centers_



    
   
plt.scatter(data['Age'], data['Bilirubin'], c=labels)
plt.scatter(centroids[:, 3], centroids[:, 9], marker='x', color='red', s=100, label='Centroids')
plt.xlabel('Age')
plt.ylabel('Bilirubin')
plt.title('K-means Clustering')
plt.legend()
plt.show()