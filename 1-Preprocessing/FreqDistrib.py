#https://pt.stackoverflow.com/questions/270580/como-fazer-uma-tabela-de-distribui%C3%A7%C3%A3o-de-frequ%C3%AAncia-em-python


import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
    input_file = '0-Datasets/Cirrhosis2.csv'
    names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
    features = ['N_Days','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
    target = 'Status'
    df = pd.read_csv(input_file, names = names) # Nome das colunas                      
   # ShowInformationDataFrame(df,"Dataframe original")

if __name__ == "__main__":
    main()