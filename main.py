# запрос данных
a, b, c = (
    float(input("Введите первое число: ")),
    float(input("Введите второе число: ")),
    float(input("Введите третье число: ")),
)

# подсчет среднего, минимального, максимального
avg = (a + b + c) / 3
mini = min(a, b, c)
maxi = max(a, b, c)

# вывод получившихся значений
print(f"среднее арифметическое: {avg:.2f}")
print(f"minimum: {mini}")
print(f"maximum: {maxi}")
