#V1:Отсортировать строки В порядке увеличения разницы между количеством согласных и количеством гласных букв в строке
def count(s):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count_v = 0
    count_c = 0
    for i in s:
        if i.lower() in vowels:
            count_v += 1
        if i.lower() in consonants:
            count_c += 1
    return abs(count_c - count_v)

s_list = input("Введите список строк через двойной пробел: ").split("  ")
s_list.sort(key = lambda x: count(x))
print("Отсортированный список:")
for i in s_list:
    print(i)
