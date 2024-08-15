import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

def distancia_euclidiana(vet1, vet2):
    distancia = 0
    for i in range(len(vet1)-1):
        distancia += (vet1[i] - vet2[i])**2
    distancia = distancia**(1/2)
    return distancia

def retorna_vizinhos(base_treinamento, amostra_teste, k):
    distancias = []
    # calc toda a distancia para toda a base de treinamento
    for i in base_treinamento:
        dist = distancia_euclidiana(amostra_teste, i)
        distancias.append((i,dist))
    #ordenacao das distancias
    distancias.sort(key=lambda tup: tup[1])
    vizinhos = []
    for i in range(k):
        vizinhos.append(distancias[i][0])
    
    return vizinhos

def classifica(base_treinamento, amostra_teste, k):
    vizinhos = retorna_vizinhos(base_treinamento, amostra_teste, k)
    rotulos = [v[-1] for v in vizinhos]
    predicao = max(set(rotulos), key=rotulos.count)
    return predicao

def plota_matriz_confusao(y_verdadeiro, y_predito):
    matriz_confusao = confusion_matrix(y_verdadeiro, y_predito)
    plt.figure(figsize=(10, 7))  # Aumenta o tamanho da figura
    sns.heatmap(matriz_confusao, annot=True, fmt="d", cmap="Blues", cbar=False, annot_kws={"size": 16})
    plt.xlabel('Predito', fontsize=14)
    plt.ylabel('Verdadeiro', fontsize=14)
    plt.title('Matriz de Confusão', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

def main():
    print('KNN')
    treinamento = [[1, 2, 0],
                   [2, 3, 0],
                   [2, 1, 0],
                   [2, 2, 1],
                   [6, 7, 1],
                   [7, 7, 1],
                   [5, 5, 1]
                   ]
    teste = [5, 6, 1]
    k = 3  # Ajuste o valor de k conforme necessário
    
    predicao = classifica(treinamento, teste, k)
    print('Resultado da classificação')
    print('Rótulo esperado: %i\nRótulo Predito: %i\n' % (teste[-1], predicao))
    
    amostras_teste = [[5, 6, 1], [2, 2, 0], [6, 6, 1], [3, 3, 0]]
    y_verdadeiro = [amostra[-1] for amostra in amostras_teste]
    y_predito = [classifica(treinamento, amostra, k) for amostra in amostras_teste]
    
    plota_matriz_confusao(y_verdadeiro, y_predito)

if __name__ == '__main__':
    main()
