# E.Plotnychenko
# Игра "Угадай число"
# Генератор псевдослучайных чисел задаёт число от 0 до 10, пользователь должен с помощью подсказок угадать число
import random

user_name = input(print("Hello. What's your name? "))
user_number = 11

number = random.randrange(0, 10)
print("I thought of a number. Try to guess")

while user_number != number:
    user_number = int(input("Enter an integer from 0 to 10 "))
    if user_number < number:
        print("Try again. Enter a number greater")
    else:
        print("Try again. Enter a number less")
print(f"{user_name}, Congratulations!!! It's a {number}")
