# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# a a a b c a a d c d d
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

chars = input().split()
dict_chars = {}.fromkeys(chars, 0)

for i in chars:
    print(f"{i}_{dict_chars[i]}" if dict_chars[i] else i, end=" ")
    dict_chars[i] += 1