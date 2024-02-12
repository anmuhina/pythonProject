#V58:Для введенного списка вывести количество элементов, которые
#могут быть получены как сумма двух любых других элементов списка
def count(arr, elem):
    for j in range(len(arr)):
        for k in range(j + 1, len(arr)):
            if elem == arr[j] + arr[k]:
                return 1
    return -1

#s = [1, 2, 3, 4, 5]
s = input("Введите элементы списка через пробел:")
arr_str = s.split()
arr_int = [int(i) for i in arr_str]
c = 0
for i in arr_int:
    if count(arr_int, i) == 1:
        c += 1
print("Количество элементов списка, которые могут быть получены как сумма двух любых других элементов:", c)
