# Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым
#
# Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1 и n(само число)

def is_prime_number(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    for i in range(3, int((n ** 0.5) + 1), 2):
        if (n % i == 0):
            return False
    return True


print(is_prime_number(int(input())))