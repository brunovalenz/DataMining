import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Função para plotar a matriz de confusão
def plot_confusion_matrix(cm, target_names, normalize=False, title='Confusion Matrix'):
    plt.figure(figsize=(10, 7))
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)#0[:, np.newaxis]
    sns.heatmap(cm, annot=True, fmt='.2f' if normalize else 'd', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
    plt.title(title)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

# Carregar a base de dados de cirrose
names = ['N_Days','Status','Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage'] 
features = ['N_Days', 'Status', 'Drug','Age','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
data = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Pré-processamento dos dados
# Supondo que a coluna 'target' seja a variável alvo e o resto sejam características
X = data.drop('Status', axis=1)
y = data['Status']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Exibir vetores de suporte
print(svm.support_vectors_)
print(svm.support_)
print("Qtd Support vectors: ")
print(svm.n_support_)

# Prever usando o conjunto de teste
y_hat_test = svm.predict(X_test)

# Obter a acurácia e F1 score
accuracy = accuracy_score(y_test, y_hat_test) * 100
f1 = f1_score(y_test, y_hat_test, average='macro')
print("Acurracy SVM from sk-learn: {:.2f}%".format(accuracy))
print("F1 Score SVM from sk-learn: {:.2f}%".format(f1))

# Obter a matriz de confusão
cm = confusion_matrix(y_test, y_hat_test)
target_names = ['Classe 0', 'Classe 1']  # Substitua pelos nomes reais das classes
plot_confusion_matrix(cm, target_names, False, "Confusion Matrix - SVM sklearn")
plot_confusion_matrix(cm, target_names, True, "Confusion Matrix - SVM sklearn normalized")