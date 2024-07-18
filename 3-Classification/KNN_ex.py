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
    #print(distancias)
    vizinhos = []
    for i in range(k):
      vizinhos.append(distancias[i][0])
    
    return vizinhos

def classifica(base_treinamento,amostra_teste,k):
    vizinhos = retorna_vizinhos(base_treinamento,amostra_teste,k)

    rotulos = [v[-1] for v in vizinhos]
    print(rotulos)
    predicao = max(set(rotulos), key=rotulos.count)
    return predicao

def main():
    print('KNN')
    treinamento =[ [1,2, 0],
                   [2,3, 0],
                   [2,1, 0],
                   [2,2, 1],
                   [6,7, 1],
                   [7,7, 1],
                   [5,5, 1]
                   ]
    teste = [5,6, 1]
    predicao = classifica(treinamento,teste,7)
    print('Resultado da classificacao')
    print('Rotulo esperado: %i\nRotulo Predicao: %i\n' % (teste[-1],predicao))

if __name__ == '__main__':
    main()