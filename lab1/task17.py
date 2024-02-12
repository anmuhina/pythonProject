#V34:Дан целочисленный массив и отрезок a..b. Необходимо найти элементы, значение которых принадлежит этому отрезку
def elemsFromSegment(arr, a, b):
    new_arr = []
    for i in arr:
        if a <= i <= b and i not in new_arr:
            new_arr.append(i)
    return new_arr

s = input("Введите элементы массива через пробел:")
arr_str = s.split()
arr_int = [int(i) for i in arr_str]
a = int(input("Введите начало a отрезка [a,b]:"))
b = int(input("Введите конец b отрезка [a,b]:"))
print("Элементы массива, значения которых принадлежат данному отрезку:", elemsFromSegment(arr_int, a, b))
