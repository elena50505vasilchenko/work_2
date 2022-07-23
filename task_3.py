seasons = ["Весна", "Лето", "Осень", "Зима"]
seasons_1 = {1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
num = int(input("Введите число: "))
if 5 >= num >= 3:
    print(seasons[0])
    print(seasons_1.get(1))
elif 8 >= num >= 6:
    print(seasons[1])
    print(seasons_1.get(2))
elif 11 >= num >= 8:
    print(seasons[2])
    print(seasons_1.get(3))
elif num == 1 or num == 2 or num == 12:
    print(seasons[3])
    print(seasons_1.get(4))
else:
    print("Ошибка ввода")
