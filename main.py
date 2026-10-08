# импортируем либу для работы со строками
import string

# ввод данных
text = input("Строка: ")

# подсчет всех сущностей строки
letters = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)
spaces = sum(c.isspace() for c in text)
punct = sum(c in string.punctuation for c in text)

# вывод соответственно всех сущностей
print("Буквы:", letters)
print("Цифры:", digits)
print("Пробелы:", spaces)
print("Знаки препинания:", punct)
