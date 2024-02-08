#V15:Дано натуральное число. Необходимо найти количество различных цифр в его десятичной записи
def count(n):
    s = str(n)
    unique = []
    for i in s:
        if i in unique:
            continue
        else:
            unique.append(i)
    return len(unique)

#n = 12345666677788222111133344455578
n = int(input("Введите натуральное число:"))
print("Количество различных цифр в записи данного числа:", count(n))
