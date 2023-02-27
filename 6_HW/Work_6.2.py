# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

import random
mas = [random.randint(-50, 50) for i in range(random.randint(10,20))]
print(*mas)
max = int(input("MAX = "))
min = int(input("MIN = "))
new_mas = []
if max >= min:
    for i in range(len(mas)):
        if max >= mas[i] and min <= mas[i]:
            new_mas.append(i)
print("Количество: ", len(new_mas))
print("Индексы: ", new_mas)