# Задача 9. Вариант 16.
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен
# его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток
# узнать, есть ли какая-либо буква в слове, причем программа может отвечать только
# "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

# Смирнов Н.Н.
# 17.03.2017

import random

WORDS = ("звездопад", "отвернись", "парцелляция", "листопад")
word = random.choice(WORDS)
quantity_letter_in_word = len(word)
j = 0

print("""
    Компьютер выбрал слово. Вы должны его отгадать. 
    Вам будет известно количество букв в слове и
    предоставлено ровно пять попыток узнать 
    присутствует ли та или иная буква.
    После этого вы должны будете угадать целое слово. 
    """)

print("Количество букв в слове:", quantity_letter_in_word)
while True:
    while j != 5:
        player_version = input("Введите букву чтобы проверить её присутствие в слове: \n")
        if player_version.lower() in word:
            print("Да")
        else:
            print("Нет")
        j += 1

    answer = input("Ваш ответ? : \n")
    if answer.lower() != word:
        print("Вы не угадали. Попробуем ещё раз.")
        j = 0
    else:
        break

print("\nВы угадали. Поздравляем!")


input("\n\nНажмите Enter, чтобы выйти.")