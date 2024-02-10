#V10:Отсортировать строки В порядке увеличения среднего количества «зеркальных» троек (например, «ada»)
#символов в строке
def count(s):
    k = 0
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            k += 1
    return k

s_list = input("Введите список строк через двойной пробел: ").split("  ")
s_list.sort(key=lambda x: count(x))
print("Отсортированный список:")
for i in s_list:
    print(i)
