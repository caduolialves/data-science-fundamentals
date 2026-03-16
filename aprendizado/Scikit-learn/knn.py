import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
import seaborn as sns


"""
Carregar o dataset iris e dividir em duas variáveis.

x = Features(características das flores)
y = Target(0, 1 ou 2, referente a Setosa, Versicolor e Virginica)
"""

x, y = load_iris(return_X_y=True)
x = pd.DataFrame(x, columns=load_iris()['feature_names']) # transforma ndarray
# em dataframe e adiciona nome as colunas.
y = pd.DataFrame(y, columns=['Target'])
y_label = y.replace([0,1,2],['setosa', 'versicolor', 'virginica'])

iris = pd.concat((x,y_label), axis=1) # junta os DataFrames com axis=1(verticalmente)

x.shape # verificando o shape (150,4)

# Como não da pra plotar 4 dimensões, vamos plotar os pares de variáveis
# para visualização da distribuição em um espaço 2D.

sns.pairplot(iris, hue='Target', palette='bright');

# Visualizando o plot, vemos que é possível utilizar o knn pelo motivo de
# que os targets estão bem separados uns dos outros.

"""
Separando o dataset em Treino e Teste
"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

"""
Criando, treinando e usando o KNN
"""

# Cria uma instancia do modelo de classificação KNN
knn = KNeighborsClassifier(n_neighbors=5, # Define o numero de vizinhos
                           weights='uniform') # Cada vizinho tem o mesmo peso, podemos usar distance, assim, o vizinho mais próximo terá maior peso

# Realiza o treino (armazena os dados de treinamento)
# O KNN diferentemente de outros modelos como o de Regressão Linear, Logística,
# não cria uma equação nem ajusta parâmetros, ele apenas guarda os dados
knn.fit(x_train, y_train)


# Faz a previsão com os dados de treino, pegando cada ponto de x_train e
# perguntando, quais são os 5 vizinhos mais próximos? depois retorna y_train_pred
y_train_pred = knn.predict(x_train)
y_test_pred = knn.predict(x_test)

print("Acurácia na base de teste: ", accuracy_score(y_test, y_test_pred))

knn.predict([[0,1,0,0]])