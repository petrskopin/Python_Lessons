"""
ЗАДАЧА:
2.	Поместите построенную модель в класс
a.	все гипер параметры принимаются при инициализации
b.	методы:
i.	подготовка данных
ii.	обучение
iii.	инференс (прямой проход сети по обученным весам)
"""

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

class MyNeuralNetwork:
    def __init__(self, units1, input_dim, activation1, units2, activation2, units3, activation3, loss, optimizer,
                 metrics, epochs, batch_size, verbose):
        self.units1 = units1
        self.input_dim = input_dim
        self.activation1 = activation1
        self.units2 = units2
        self.activation2 = activation2
        self.units3 = units3
        self.activation3 = activation3
        self.loss = loss
        self.optimizer = optimizer
        self.metrics = metrics
        self.epochs = epochs
        self.batch_size = batch_size
        self.verbose = verbose

    def prepare_data(self):
        self.dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)
        self.Y = self.dataset[:, -1]
        self.X = self.dataset[:, :8]

    def study(self):
        self.model = Sequential()
        self.model.add(Dense(self.units1, input_dim=self.input_dim, activation=self.activation1))
        self.model.add(Dense(self.units2, activation=self.activation2))
        self.model.add(Dense(self.units3, activation=self.activation3))

        self.model.compile(loss=self.loss, optimizer=self.optimizer, metrics=self.metrics)
        self.model.fit(self.X, self.Y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose)


    def run(self):
        self.predictions = self.model.predict(np.array(self.X))

NN1 = MyNeuralNetwork(12, 8, 'relu', 8, 'relu', 1, 'sigmoid',
                      'binary_crossentropy', 'adam', ['accuracy'], 15, 10, 2)
NN1.prepare_data()
NN1.study()
NN1.run()

