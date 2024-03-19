import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Carregar os dados
input_file = '0-Datasets/cirrhosis2Clear.csv'
names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
features = ['Age', 'Bilirubin', 'Cholesterol']  # Variáveis para o gráfico 3D
dados = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Criar a figura e o eixo 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotar o gráfico de dispersão 3D
ax.scatter(dados['Age'], dados['Bilirubin'], dados['Cholesterol'], color='b')

# Adicionar rótulos aos eixos
ax.set_xlabel('Idade')
ax.set_ylabel('Bilirrubina')
ax.set_zlabel('Colesterol')

# Mostrar o gráfico
plt.show()
