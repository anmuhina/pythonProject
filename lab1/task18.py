#V46:Дан целочисленный массив. Необходимо вывести вначале его положительные элементы, а затем – отрицательные
def sortArray(arr):
    pos = []
    neg = []
    for i in arr:
        if i >= 0 and i not in pos:
            pos.append(i)
        if i < 0 and i not in neg:
            neg.append(i)
    return pos + neg

s = input("Введите элементы массива через пробел:")
arr_str = s.split()
arr_int = [int(i) for i in arr_str]
print(sortArray(arr_int))
