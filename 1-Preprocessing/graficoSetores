import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
input_file = '0-Datasets/cirrhosis2Clear.csv'
names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
features = ['Status']  # Variável categórica para o gráfico de setores
dados = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Contar a ocorrência de cada categoria
contagem = dados['Status'].value_counts()

# Plotar o gráfico de setores
plt.figure(figsize=(8, 6))
plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=140)

# Adicionar título
plt.title('Distribuição de Status')

# Mostrar o gráfico
plt.axis('equal')  # Mantém o aspecto igual para que o gráfico seja um círculo
plt.show()