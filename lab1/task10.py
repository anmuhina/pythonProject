#Дан список строк с клавиатуры. Упорядочить по количеству слов в строке
s_list = input("Введите список строк через двойной пробел: ").split("  ")
s_list.sort(key = lambda x: len(x.split()))
print("Отсортированный список:")
for i in s_list:
    print(i)
