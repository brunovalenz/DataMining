import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Suponha que você tenha um DataFrame chamado df com os dados normalizados
# Se os dados não estiverem normalizados, você pode normalizá-los usando StandardScaler

# Exemplo de normalização (descomente se necessário)
# scaler = StandardScaler()
# df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Para este exemplo, vamos usar uma base de dados fictícia normalizada

names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
df_normalized = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes
 

# Definir o número de clusters
num_clusters = 3

# Aplicar o KMeans
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df_normalized['cluster'] = kmeans.fit_predict(df_normalized)

# Visualizar os resultados com Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Bilirubin', hue='cluster', palette='viridis', data=df_normalized, s=100)
plt.title('K-Means Clustering')
plt.show()
