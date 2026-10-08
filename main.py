# вывод опций
print("Конвертер температур")
print("1. Из °C в °F")
print("2. Из °F в °C")

# запрос опции
choice = input("Ваш выбор (1/2): ")

# условие для правильной конвертировки
if choice == "1":
    # запрос данных (температура в цельсиях)
    celsius = float(input("Введите температуру в °C: "))
    # вычисление фаренгейта
    fahrenheit = celsius * 9 / 5 + 32
    # вывод конвертирования
    print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
elif choice == "2":
    # запрос данных (температура в фаренгейтах)
    fahrenheit = float(input("Введите температуру в °F: "))
    # вычисление цельсия
    celsius = (fahrenheit - 32) * 5 / 9
    # вывод конвертирования
    print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")
else:
    print("Некорректный выбор")
