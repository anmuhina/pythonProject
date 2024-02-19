#Вариант 10. Забастовки

print("Введите числа N и K через пробел:")
N, K = map(int, input().split())

daysOfStrike = set()
schedule = {}

print("Введите K строк со значениями ai и bi через пробел:")
for i in range(K):
    a, b = map(int, input().split())
    schedule[a] = b

for a, b in schedule.items():
    day = a
    while day <= N:
        if day % 7 != 6 and day % 7 != 0:
            daysOfStrike.add(day)
        day += b

strikesInTotal = len(daysOfStrike)
print("Число забастовок, прошедших в данной стране за год:", strikesInTotal)
