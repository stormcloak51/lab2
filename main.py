# запрос данных
weight = float(input("Вес (кг): "))
height = float(input("Рост (м): "))

# подсчет имт
imt = weight / (height**2)
# вывод имт
print(f"ИМТ: {imt:.1f}")

