import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import metrics
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# 1. Carregar a base de dados
# Suponha que o arquivo CSV esteja no mesmo diretório do script ou forneça o caminho completo

names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
df = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep = ",",
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='NA')      # Define que NA será considerado valores ausentes

# 2. Explorar os dados
print(df.head())
print(df.info())
print(df.describe())

# 3. Pré-processar os dados
# Separe as características (X) e o rótulo (y)
# Suponha que o DataFrame tenha a coluna 'target' como rótulo e o resto como características
X = df.drop('Status', axis=1)
y = df['Status']

# Se necessário, normalize ou padronize os dados
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X = scaler.fit_transform(X)

# 4. Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Treinar a árvore de decisão
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# 6. Fazer previsões no conjunto de teste
y_pred = clf.predict(X_test)

# Avaliar a precisão do modelo
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 7. Visualizar a árvore de decisão
#plt.figure(figsize=(12, 8))
#plot_tree(clf, feature_names=X.columns, class_names=str(set(y)), filled=True)
#plt.title("Decision Tree")
#plt.show()
clf = DecisionTreeClassifier(max_leaf_nodes=3)
clf.fit(X_train, y_train)
tree.plot_tree(clf)
plt.show()