#V15:Дана строка. Необходимо подсчитать количество цифр в этой строке, значение которых больше 5
import re
def count(s):
    k = 0
    for i in s:
        if i.isdigit() and int(i)>5:
            k += 1
    return k

#s = "8v  fsju 9 hjw 3 6 7fhys 28"
s = input("Введите строку:")
print(count(s))
