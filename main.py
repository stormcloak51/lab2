# запрос данных у пользователя
number = int(input("Введите число: "))
drobnoe = float(input("Введите дробное число: "))
string = input("Введите строку: ")

# вывод типов и значений
print(f"Значение: {number}, тип: {type(number).__name__}")
print(f"Значение: {drobnoe}, тип: {type(drobnoe)}")
print(f"Значение: {string}, тип: {type(string).__name__}")

