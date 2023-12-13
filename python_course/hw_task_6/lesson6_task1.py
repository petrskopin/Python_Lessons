"""
ЗАДАЧА:
1.	Постройте модель обучения по файлу data.txt, с использованием библиотеки Keras.
a.	В моделе сделайте 3 слоя
i.	12 нейронов, функция активации - relu
ii.	8 нейронов, функция активации - relu
iii.	1 нейрон, функция активации - sigmoid
b.	Функция ошибки - binary_crossentropy
c.	оптимизатор - adam
d.	Запустите обучение с таким набором параметров:
i.	epochs=15, batch_size=10, verbose=2
e.	Сделайте предсказание по первым трем строкам датасета.

"""

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)

Y = dataset[:, -1]
X = dataset[:, :8]

#Создаем модель
model = Sequential()
model.add(Dense(12, input_dim=8,activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#Обучение
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=15, batch_size=10, verbose=2)

#предсказание
predictions_0 = model.predict(np.array(X[:3]))
print(predictions_0, Y[:3])
