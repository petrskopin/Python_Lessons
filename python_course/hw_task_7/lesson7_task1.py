"""
ЗАДАЧА:
2.	Сделайте предсказание выживаемости пассажира, на основе датасета “titanic.csv”,
с использованием библиотеки sklearn. Сделайте тестовый проход на 10 пассажирах.
"""
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

#читаем pandas, потому что numpy падает из-за запятых в поле Name
titanic_pd = pd.read_csv('titanic.csv')
print(titanic_pd["Name"])


#Удаляем лишние столбцы
titanic_pd = titanic_pd.drop(['PassengerID'], axis='columns')
titanic_pd = titanic_pd.drop(['Name'], axis='columns')
titanic_pd = titanic_pd.drop(['Sex'], axis='columns')
#Фильтруем мусор из Age
titanic_pd = titanic_pd[titanic_pd['Age'] > 0]


#превращаем значимые в числа
titanic_pd.loc[titanic_pd['PClass'] == '1st', 'PClass'] = 1
titanic_pd.loc[titanic_pd['PClass'] == '2nd', 'PClass'] = 2
titanic_pd.loc[titanic_pd['PClass'] == '3rd', 'PClass'] = 3

# Кладем в Y столбец Survived
Y = np.array(titanic_pd["Survived"])

#В X всё кроме Y
titanic_pd = titanic_pd.drop(['Survived'], axis='columns')
X = np.array(titanic_pd)

model = svm.SVC()
model.fit(X, Y)
predicted = model.predict(X[0:10])
print("Предсказание:", predicted)
print("Фактически:", Y[0:10])

