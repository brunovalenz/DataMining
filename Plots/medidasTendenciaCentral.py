import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando os dados
names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
features = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
dados = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Calculando as estatísticas para cada variável
estatisticas = {}
for coluna in dados.columns:
    estatisticas[coluna] = {
        'Média': dados[coluna].mean(),
        'Moda': dados[coluna].mode().values[0],
        'Mediana': dados[coluna].median(),
        'Ponto Médio': (dados[coluna].max() + dados[coluna].min()) / 2,
        'Média Geométrica': np.prod(dados[coluna]) ** (1 / len(dados[coluna]))
    }

# Criando um gráfico de barras para cada estatística
plt.figure(figsize=(14, 10))
for i, (coluna, valores) in enumerate(estatisticas.items(), start=1):
    plt.subplot(5, 4, i)
    plt.bar(list(valores.keys()), list(valores.values()), color=['skyblue', 'lightcoral', 'lightgreen', 'orange', 'lightpink'])
    plt.title(coluna)

plt.tight_layout()
plt.show()
