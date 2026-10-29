n = int(input("Введите число: "))

print(bin(n)[2:])

if n == 0:
    result = "0"
else:
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2

print(result)
