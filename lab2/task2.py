#Вариант 10. Продажи

listOfSales = {}

print("Введите данные о продажах каждый раз с новой строки, по окончании ввода добавьте двойной enter:")
while True:
    s = input()
    if (s==""):
        break
    name, product, amount = s.split()
    if name not in listOfSales:
        listOfSales[name] = {}
    if product not in listOfSales[name]:
        listOfSales[name][product] = 0
    listOfSales[name][product] += int(amount)


buyers = sorted(listOfSales.keys())
print("Отсортированные данные о покупателях:")
for buyer in buyers:
    products = sorted(listOfSales[buyer].keys())
    print("Buyer:", buyer)
    for product in products:
        print(product, ":", listOfSales[buyer][product])
    print("\n")
