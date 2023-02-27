# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую 
# cтепень B с помощью рекурсии.

def degree(a, b):
    if b == 0:
        return 1
    return degree(a, b - 1) * a
print(degree(int(input()), int(input())))