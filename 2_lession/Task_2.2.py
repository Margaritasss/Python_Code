# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# 1 2 3 4 5 6 7 8 9 10 11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

num = int(input())
f_1 = 0
f_2 = 1
i = 2
while f_2 <= num:
    if num == f_2:
        print(i)
        break
    f_1, f_2 = f_2, f_1 + f_2
    i += 1
else:
    print(-1)
