"""
ЗАДАЧА:
2.	В DataFrame из предыдущего задания добавьте индексы строк в виде латинских букв. Выведите на печать строку в которой все числа > 5, если такая есть
"""

import pandas as pd
import numpy as np

# датафрейм из предыдущего задания:
df1 = pd.DataFrame(np.random.randint(1, 11, size=( 10, 10)))

df1['index'] = ['A','B','C','D','E','F','G','H','I','K']
df2 = df1.set_index('index')

#дальше очень корявое решение, но ничего лучше я не придумал:
df2['min_val'] = df2.min(axis=1)
print(df2[df2.min_val > 5])