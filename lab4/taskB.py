#B
file2 = open("file2.txt")
n = int(file2.readline())
list_of_kg = [int(file2.readline()) for i in range(n)]

min_cost = 10**20
best_point = -1

kg_in_total = sum(list_of_kg)

#Вычисляем количество мусора на каждом пункте сбора c учетом их распределения
kg_in_points = [0]*n
kg_in_points[0] = sum(list_of_kg[0:n//2])
for i in range(1, n):
    kg_in_points[i] = kg_in_points[i-1] - list_of_kg[i-1] + list_of_kg[((i-1) + n//2) % n]

#Вычисляем разницу между общим кол-вом мусора и кол-вом на каждом пункте
dif = [0]*n
for i in range(n):
    dif[i] = kg_in_total-kg_in_points[i]

#Цена для каждого пункта с учетом их распределения
price = [0]*n
for i in range(n//2):
    price[0] += list_of_kg[i]*i
for i in range(n//2, n):
    price[0] += list_of_kg[i]*(n-i)
for i in range(1, n):
    price[i] = price[i-1] - kg_in_points[i] + dif[i]
    if price[i] < min_cost:
        min_cost = price[i]
        best_point = i

print("Номер пункта: " + str(best_point+1) + "\nМинимальная стоимость: " + str(min_cost))
