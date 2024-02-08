#V4:Дана строка. Необходимо подсчитать количество чисел в этой строке, значение которых меньше 5
import re
def count(s):
    reg = r"[-]?\d*\.\d+|\d+"
    k=0
    l = []
    c = re.findall(reg, s)
    for i in range(0, len(c)):
        if float(c[i])<5:
            k += 1
    return k

#print(count("1 -2.5 xn 5.5 aw 3.5 jf 4 10 ewjn -7.9028"))
s = input("Введите строку:")
print("Количество чисел в данной строке, значение которых меньше 5:", count(s))
