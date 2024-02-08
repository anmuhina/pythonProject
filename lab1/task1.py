from cmath import sqrt

# функция 1
def nod(a, b):
    while b:
        a, b = b, a%b
    return a

def count(n):
    k = 0
    for i in range(2, n + 1, 2):
        if nod(i, n) != 1:
            k += 1
    return k


# функция 2
def maxNumber(n):
    max = -1
    while n:
        a = n % 10
        if a % 3 != 0 and a > max:
            max = a
        n //= 10
    return max


# функция 3
def sum(n):
    s = 0
    while n:
        a = n % 10
        if a < 5:
            s += a
        n //= 10
    return s

def minDivisor(n):
    min = 0
    if n == 1:
        min = 1
    else:
        for i in range(2, n + 1):
            if (n % i == 0):
                min = i
    return min

def maxNotPrime(n):
    max = 0
    for i in range(n - 1, 1, -1):
        if nod(i, n) != 1 and i % minDivisor(n) != 0:
            max = i
            break
    return max

def multipl(n):
    return sum(n) * maxNotPrime(n)


n = 10
res = count(n)
print("1) количество четных чисел, не взаимно простых с данным:",res)
k = 1283695
res1 = maxNumber(k)
print("2) максимальная цифра числа, не делящаяся на 3:",res1)
m = 125
res2 = multipl(m)
print("3) произведение максимального числа, не взаимно простого с данным, не делящегося на наименьший делитель исходно числа, и суммы цифр числа, меньших 5:",res2)
