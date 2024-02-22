#A
file1 = open("file1.txt")
n = int(file1.readline())
list_of_kg = [int(file1.readline()) for i in range(n)]

min_cost = 10**20
best_point = -1

for point in range(n):
    cost_of_delivery = 0
    for i in range(n):
        min_dist = min(abs(point - i), n - abs(point - i))
        cost_of_delivery += min_dist*list_of_kg[i]
    if cost_of_delivery < min_cost:
        min_cost = cost_of_delivery
        best_point = point

print("Номер пункта: " + str(best_point+1) + "\nМинимальная стоимость: " + str(min_cost))
