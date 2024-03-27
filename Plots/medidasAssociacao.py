import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
features = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
dados = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Calculando a matriz de covariância
covariance_matrix = dados.cov()

# Calculando a matriz de correlação
correlation_matrix = dados.corr()

# Plotando o gráfico de covariância
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(covariance_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar().set_label('Covariance')
plt.title('Matriz de Covariância')
plt.xticks(ticks=range(len(features)), labels=features, rotation=90)
plt.yticks(ticks=range(len(features)), labels=features)

# Plotando o gráfico de correlação
plt.subplot(1, 2, 2)
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar().set_label('Correlation Coefficient')
plt.title('Matriz de Correlação')
plt.xticks(ticks=range(len(features)), labels=features, rotation=90)
plt.yticks(ticks=range(len(features)), labels=features)

plt.tight_layout()
plt.show()
