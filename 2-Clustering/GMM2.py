import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import pandas as pd

# Suponha que você tenha um DataFrame chamado df com os dados normalizados

# Para este exemplo, vamos usar uma base de dados fictícia normalizada
names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
df_normalized  = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')

# Definir o número de clusters
num_clusters = 3

# Aplicar o GMM
gmm = GaussianMixture(n_components=num_clusters, random_state=42)
df_normalized['cluster'] = gmm.fit_predict(df_normalized)

# Visualizar os resultados com Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Bilirubin', hue='cluster', palette='viridis', data=df_normalized, s=100)
plt.title('GMM Clustering')
plt.show()
