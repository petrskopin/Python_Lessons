"""ЗАДАЧА:
10)	* Замените классическое представление цикла for в примере на любую конструкцию, так чтоб результат оставался тот же.
"""

# совсем не понял задачу, но допустим тоже самое через while
lst = [2, 4, 5, 8, 9, 13]

counter = 0
while counter < len(lst):
    lst[counter] = lst[counter] * counter
    counter += 1

print(lst)
