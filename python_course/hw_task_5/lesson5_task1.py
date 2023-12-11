"""
ЗАДАЧА:
1.	Создайте DataFrame с рандомными целыми числами от 1 до 10, размером 10х10.
"""
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(1, 11, size=( 10, 10)))
print(df1)