from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score  # Importa a função f1_score

def main():
    names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage'] 
    features = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
    input_file = '0-Datasets/cirrhosis2Clear.csv'
    target = 'Status'
    
    # Carregar os dados
    df = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

    # Separando as características
    X = df.loc[:, features].values
    print(X.shape)

    # Separando o alvo
    y = df.loc[:, [target]].values.ravel()  # Converte y para um array unidimensional

    # Padronizando as características
    X = StandardScaler().fit_transform(X)
    
    # Dividindo os dados em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    print(X_train.shape)
    print(X_test.shape)

    # Treinando o modelo de árvore de decisão
    clf = DecisionTreeClassifier(max_leaf_nodes=6)
    clf.fit(X_train, y_train)
    
    # Plotando a árvore de decisão
    plt.figure(figsize=(20,10))
    tree.plot_tree(clf, feature_names=features, class_names=list(map(str, set(y))), filled=True)
    plt.show()
    
    # Fazendo previsões
    predictions = clf.predict(X_test)
    print(predictions)
    
    # Calculando a acurácia
    accuracy = clf.score(X_test, y_test)
    print('Acurácia:')
    print(accuracy)
    
    # Calculando o F1 Score
    f1 = f1_score(y_test, predictions, average='weighted')
    print('F1 Score:')
    print(f1)

if __name__ == "__main__":
    main()
