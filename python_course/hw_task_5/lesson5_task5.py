"""
ЗАДАЧА:
5.	Создайте DataFrame из файла emojis.csv.
a.	Получите количество созданных эмоджи за каждый год
b.	Постройте график
"""

import pandas as pd
import matplotlib.pyplot as plt

emojis = pd.read_csv('emojis.csv')
plt.plot(emojis.groupby('Year')['Year'].count())
plt.show()