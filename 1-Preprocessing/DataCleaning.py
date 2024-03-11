import pandas as pd
import numpy as np

def main():
    # Faz a leitura do arquivo
    names = ['ID','N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
    features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
    output_file = '0-Datasets/cirrhosis2Clear.csv'
    input_file = '0-Datasets/cirrhosis2.csv'
    df = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ";",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='?')      # Define que ? será considerado valores ausentes
    
    df_original = df.copy()
    # Imprime as 15 primeiras linhas do arquivo
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(15))
    print("\n")        

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")
    
    # Imprime uma analise descritiva sobre dos dados
    print("DESCRIÇÃO DOS DADOS\n")
    print(df.describe())
    print("\n")
    
    # Imprime a quantidade de valores faltantes por coluna
    print("VALORES FALTANTES\n")
    print(df.isnull().sum())
    print("\n")    
    
    columns_missing_value = df.columns[df.isnull().any()]
    print(columns_missing_value)
    method = 'mode' # number or median or mean or mode
    
    for c in columns_missing_value:
        UpdateMissingValues(df, c)
    
    cat_columns = df.select_dtypes(['object']).columns
    df[cat_columns] = df[cat_columns].apply(lambda x: pd.factorize(x)[0])

    print("COLUNAS QUE SERÃO MUDADAS:")
    print(cat_columns)
    print("--------------------------------------")
    print(df.describe())
    print("\n")
    print(df.head(15))
    print(df_original.head(15))
    print("\n")
    
    # Salva arquivo com o tratamento para dados faltantes
    df.to_csv(output_file, header=False, index=False)  
    

def UpdateMissingValues(df, column, method="mode", number=0):
    if method == 'number':
        # Substituindo valores ausentes por um número
        df[column].fillna(number, inplace=True)
    elif method == 'median':
        # Substituindo valores ausentes pela mediana 
        median = df[column].median()
        df[column].fillna(median, inplace=True)
    elif method == 'mean':
        # Substituindo valores ausentes pela média
        mean = df[column].mean()
        df[column].fillna(mean, inplace=True)
    elif method == 'mode':
        # Substituindo valores ausentes pela moda
        mode = df[column].mode()[0]
        df[column].fillna(mode, inplace=True)


if __name__ == "__main__":
    main()