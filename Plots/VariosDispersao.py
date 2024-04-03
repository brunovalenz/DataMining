import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
dados = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes

# Função para plotar gráfico de dispersão
def scatter_vs_column(data, chosen_column):
    # Selecionar as colunas que não são a escolhida
    other_columns = [col for col in data.columns if col != chosen_column]
    
    # Configurações da janela de plotagem
    num_plots = len(other_columns)
    num_cols = 3
    num_rows = (num_plots - 1) // num_cols + 1
    
    # Criar os subplots e plotar os dados
    plt.figure(figsize=(15, 5*num_rows))
    for i, col in enumerate(other_columns, start=1):
        plt.subplot(num_rows, num_cols, i)
        plt.scatter(data[chosen_column], data[col], alpha=0.5)
        plt.xlabel(chosen_column)
        plt.ylabel(col)
        plt.title(f'{chosen_column} vs {col}')
    
    # Ajustar o layout e mostrar o gráfico
    plt.tight_layout()
    plt.show()

# Escolha da coluna
chosen_column = 'SGOT'

# Plotar gráficos de dispersão para a coluna escolhida versus todas as outras colunas
scatter_vs_column(dados, chosen_column)
