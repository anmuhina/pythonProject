#V4: Дана строка. Необходимо проверить, является ли она палиндромом.
def palindrom(s):
    s = s.lower()
    s1 = s.split()
    s2 = ''.join(s1)
    return s2 == s2[::-1]

#s = "А роза упала на лапу азора"
s=input('Введите строку:')
if palindrom(s):
    print('Данная строка является палиндромом')
else:
    print('Данная строка не является палиндромом')
