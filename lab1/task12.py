#V5:Отсортировать строки В порядке увеличения квадратичного отклонения частоты встречаемости самого часто
#встречаемого в строке символа от частоты его встречаемости в текстах на этом алфавите
import math
def count_of_symbols(s, alphabet):
    list = [0] * len(alphabet)
    for i in range(len(list)):
        for j in s:
            if alphabet[i] == j:
                list[i] += 1
    return list

def deviation(text, s, alphabet):

    count_in_text = count_of_symbols(text, alphabet)

    count_in_s = count_of_symbols(s, alphabet)
    max_count_in_s = -1
    index = -1
    for i in range(len(count_in_s)):
        if count_in_s[i] > max_count_in_s:
            max_count_in_s = count_in_s[i]
            index = i
    max_freq_in_s = max_count_in_s / len(s)
    freq_in_text = count_in_text[index] / len(text)
    return (max_freq_in_s - freq_in_text) ** 2



alphabet = input("Введите алфавит:")
text = input("Введите список строк через двойной пробел: ")
s_list = text.split("  ")
s_list.sort(key = lambda x: deviation(text, x, alphabet))
print("Отсортированный список:")
for i in s_list:
    print(i)
