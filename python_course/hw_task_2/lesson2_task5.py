"""
5.	Лесенка.
Лесенкой - условный набор кубиков, в котором каждый последующий слой содержит меньше кубиков, чем предыдущий.

Напишите функцию, вычисляющую число лесенок, которое можно построить из n кубиков.
-	Длина каждой ступени может отличаться.
-	n - натуральное число в диапазоне от 1 до 100.

"""


def generate_cube_range(prev_level_cubes, left_unused_cubes):
    global global_counter
    list_of_values = []      #cписок для возможного числа кубиков этого уровня лесенки
    for i in range(prev_level_cubes+1, (left_unused_cubes+1) // 2):      #из условия что можно построить слой кубиков под этим
        list_of_values.append(i)
    if left_unused_cubes != 0:   # + добавляем все кубики в текущий уровень
        list_of_values.append(left_unused_cubes)
    print(prev_level_cubes, list_of_values) # только для дебага
    if len(list_of_values) > 1:     #если есть возможность строить следующие уровни, то строим их
        for i in list_of_values:
            generate_cube_range(i,left_unused_cubes-i)
    else:   #если мы на нижнем уровне, то увеличиваем global_counter на 1
        global_counter += 1


#В эту переменную посчитаем число построенных лесенок
global_counter = 0

#Число кубиков
N = 12

generate_cube_range(0, N) #вызываем расчет верхнего уровня лесенки (на предыдущем уровне 0 кубиков, всего N)

print("Всего возможно построить ",global_counter,"различных лесенок из", N, "кубиков")




