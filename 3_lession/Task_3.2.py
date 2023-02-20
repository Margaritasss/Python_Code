# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.


list_nums = [1, 2, 3, 4, 5]

num = int(input())
n = len(list_nums)

for i in range(0, num % n):
    list_nums.insert(0, list_nums.pop(-1))

print(list_nums)
