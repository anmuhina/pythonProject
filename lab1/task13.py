#V9:Отсортировать строки В порядке увеличения квадратичного отклонения между наибольшим ASCII-кодом символа
#строки и разницы в ASCII-кодах пар зеркально расположенных символов строки (относительно ее середины)
import math
def deviation(s):
    s_middle = len(s) // 2
    max_ascii_symbol = max(map(ord, s))
    summa = 0
    for i in range(s_middle):
        summa += (ord(s[i]) - ord(s[-i-1])) ** 2
    return math.sqrt(summa)

s_list = input("Введите список строк через двойной пробел: ").split("  ")
s_list.sort(key=lambda x: deviation(x))
print("Отсортированный список:")
for i in s_list:
    print(i)
