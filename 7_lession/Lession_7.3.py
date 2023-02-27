# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для
# разных объектов отличается - то False.
# Для пустого набора объектов,
# функция должна возвращать True.
# Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

# values = [0, 2, 10, 6]
values = [2, 3, 6, 4]


def same_by(condition, nums):
    return len(set(map(condition, nums))) == 1


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
