#ВАРИАНТ 10
import csv
import re

def time_to_seconds(str):
    res = 0
    hours_reg = re.search(r'(\d+)\s*ч', str)
    minutes_reg = re.search(r'(\d+)\s*мин', str)
    seconds_reg = re.search(r'(\d+)\s*сек', str)
    if hours_reg:
        res += int(hours_reg.group(1)) * 3600
    if minutes_reg:
        res += int(minutes_reg.group(1)) * 60
    if seconds_reg:
        res += int(seconds_reg.group(1))
    return res


list = []

with open('10 - 1.csv', encoding='utf-8') as file:
#with open('10 -2.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[9] == '-':
            total_score = None
        else:
            total_score = float(row[9].replace(',', '.'))

        scores = [float(row[i].replace(',', '.')) if row[i] != '-' else None for i in range(10, 20)]

        list.append({
            'Фамилия': row[0],
            'Имя': row[1],
            'Учреждение(организация)': row[2],
            'Отдел': row[3],
            'Адрес электронной почты': row[4],
            'Состояние': row[5],
            'Тест начат': row[6],
            'Завершено': row[7],
            'Затраченное время': row[8],
            'Оценка': total_score,
            'В.1': scores[0],
            'В.2': scores[1],
            'В.3': scores[2],
            'В.4': scores[3],
            'В.5': scores[4],
            'В.6': scores[5],
            'В.7': scores[6],
            'В.8': scores[7],
            'В.9': scores[8],
            'В.10': scores[9],
        })

count = 0
start_letter = input("Введите первую букву фамилии: ").upper()
time_in_sec = int(input("Введите требуемое время в секундах: "))

res = []
for i in list:
    if i['Фамилия'].startswith(start_letter) and time_to_seconds(i['Затраченное время']) < time_in_sec:
        count += 1
        res.append(i)

print("\n")
print("Количество людей, фамилии которых начинаются с заданной буквы, которые прошли тест меньше, чем за заданное время:", count)
for i in res:
    print(i)
