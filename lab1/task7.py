#V11:Дана строка. Необходимо найти все незадействованные символы латиницы в этой строке.
def symbols(s):
    reg = r"[a-zA-Z]"
    lat = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    used = []
    res = []
    for i in s:
        if i in lat and i not in used and i.isalpha():
            used.append(i)
    for i in lat:
        if i not in used:
            res.append(i)
    return res

#s = "AaBCDEFbcdefGgHhIiKkLMNlmnAaBc"
s = input("Введите строку:")
print(symbols(s))
