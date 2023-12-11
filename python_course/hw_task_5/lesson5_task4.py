"""
ЗАДАЧА:
4.	Создайте DataFrame из файла emojis.csv.
a.	в столбце Rank указан рейтинг смайлов, отсортированный в порядке убывания частоты. (чем чаще использовался эмоджи тем ниже значение)
b.	Выведите в консоль самую популярную подкатегорию эмоджи
"""

import pandas as pd

emojis = pd.read_csv('emojis.csv')
# группируем по Subcategory, Суммируем по столбцу Rank (считаем что чем меньше сумма тем популярнее, сортируем по возрастанию, выводим первую строку
print(emojis.groupby('Subcategory')['Rank'].sum().sort_values().head(1))