# ввод данных
seconds = int(input("Введите количество секунд: "))

# манипуляции над данными - запись колво часов, минут, секунд в переменные
hours = seconds // 3600
mins = (seconds % 3600) // 60
secs = seconds % 60

# вывод в формате чч:мм:сс
print(f"{hours:02d}:{mins:02d}:{secs:02d}")


# ДОП ЗАДАНИЕ
total_seconds = hours * 3600 + mins * 60 + secs
# проверяем равны ли значения от исходного колва секунд
print(total_seconds == seconds)
