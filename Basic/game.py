import random

# Генерируем случайное число от 1 до 100
secret_number = random.randint(1, 100)

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуйте угадать.")

attempts = 3
i = 0

while i < attempts:
    # Получаем вариант пользователя
    guess = int(input("Введите число: "))

    # Проверяем, угадал ли пользователь
    if guess == secret_number:
        print("Поздравляю! Вы угадали число!")
        break
    if guess < secret_number:
        print("Загаданное число больше.")
    if guess > secret_number:
        print("Загаданное число меньше.")
    i+=1
else:
    print("error")
    print("число было: ", secret_number)