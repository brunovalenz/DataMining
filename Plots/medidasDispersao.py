import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
features = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
dados = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Calculando a amplitude e o desvio padrão
amplitude = dados.max() - dados.min()
desvio_padrao = dados.std()

# Criando um gráfico de barras
plt.figure(figsize=(10, 6))

# Plotando a amplitude
plt.bar(amplitude.index, amplitude.values, color='skyblue', label='Amplitude')

# Plotando o desvio padrão
plt.bar(desvio_padrao.index, desvio_padrao.values, color='lightcoral', label='Desvio Padrão')

plt.title('Amplitude e Desvio Padrão das Variáveis')
plt.xlabel('Variável')
plt.ylabel('Valor')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
