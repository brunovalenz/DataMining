import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Carregando os dados
names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
features = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
dados = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Selecionando a variável para plotagem
variavel = 'Age'  # Altere para a variável desejada

# Calculando os Escores Z e os quantis
z_scores = (dados[variavel] - dados[variavel].mean()) / dados[variavel].std()
quantis = stats.probplot(dados[variavel], dist="norm", plot=None)

# Plotando o gráfico
plt.figure(figsize=(12, 6))

# Escores Z
plt.subplot(1, 2, 1)
plt.hist(z_scores, bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma dos Escores Z para ' + variavel)
plt.xlabel('Escores Z')
plt.ylabel('Frequência')

# Quantis
plt.subplot(1, 2, 2)
plt.scatter(quantis[0][0], quantis[0][1], color='lightcoral')
plt.plot(quantis[0][0], quantis[0][0], color='black', linestyle='dashed')
plt.title('Gráfico de Quantis-Quantis para ' + variavel)
plt.xlabel('Quantis Teóricos')
plt.ylabel('Quantis Observados')

plt.tight_layout()
plt.show()
