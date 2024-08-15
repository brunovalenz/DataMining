import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

# Definindo os nomes das colunas e carregando o dataset
names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema',
         'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides',
         'Platelets', 'Prothrombin', 'Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'
data = pd.read_csv(input_file, sep=",", names=names, na_values='NA')

# Separando as features numéricas e categóricas
numeric_features = ['N_Days', 'Age', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 
                    'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']
categorical_features = ['Drug', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Stage']

# Definindo a coluna de alvo
target = 'Status'  # Certifique-se de que esta é a coluna que você quer prever

# Separando as features e o target
X = data[numeric_features + categorical_features]
y = data[target]

# Lidando com valores ausentes (opcional, dependendo do dataset)
X = X.fillna(X.mean())

# Divisão em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline para pré-processamento
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Aplicando o pré-processamento aos dados
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)

# Criando o modelo da rede neural
model = tf.keras.Sequential([
    layers.InputLayer(input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Para classificação binária
])

# Compilando o modelo
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# Treinando o modelo
history = model.fit(X_train, y_train, epochs=200, validation_split=0.2, batch_size=32)

# Avaliando o modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_acc:.2f}')

# Opcional: plotando as métricas de treino
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Acurácia de treino')
plt.plot(history.history['val_accuracy'], label = 'Acurácia de validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
