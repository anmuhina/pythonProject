file3 = open("file3.txt", encoding="utf-8")
text = file3.read()

letter = input("Введите букву русского алфавита: ")

words = text.split()

count = 0
for word in words:
    if word.lower().startswith(letter):
        count += 1

print("Количество слов, начинающихся с указанной буквы: " + str(count))
