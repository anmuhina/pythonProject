#V22:Дан целочисленный массив и интервал a..b. Необходимо найти количество минимальных элементов в этом интервале
def countMin(arr, a, b):
    k = 0
    new_arr = []
    for i in arr:
        if a < i < b:
            new_arr.append(i)
    minimum = min(new_arr)
    for i in new_arr:
        if i == minimum:
            k += 1
    return k


#arr = [-1, 0, -1, 6, 2, -7, -1, 10]
#a = -5
#b = 10
s = input("Введите элементы массива через пробел:")
arr_str = s.split()
arr_int = [int(i) for i in arr_str]
a = input("Введите начало a интервала (a,b):")
b = input("Введите конец b интервала (a,b):")
print("Количество минимальных элементов в этом интервале:", countMin(arr_int, int(a), int(b)))
