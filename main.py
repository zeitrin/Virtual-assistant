import random
name_assistant = "Линда"
print("Меня зовут", name_assistant)
name = input("Как тебя зовут? ")
print("Приятно познакомиться,", name )
age = int(input("Сколько тебе лет? "))
print("Представляешь, тебе через 10 лет будет:", age + 10, "лет")
height = float(input("Какой у тебя рост? У меня 0.53 метра "))
print("Ого! Ты выше меня на", height - 0.53, "метра!" )
print("Мне очень приятно с тобой познакомиться!", name, age, "лет!", "С ростом", height, "метра!")
actions = int(input("Я могу: \n 1 - рассказать анекдот \n 2 - сложить два целых числа \n 3 - назвать любое число \n"))
if actions == 1:
        answer = int(input("1 - анекдот про наркомана \n 2 - анекдот про негра \n"))
        if answer == 1:
                print("""Нaркомaн приходит в ресторaн. Сaдится зa столик. К нему подходит офицaнт.\n Наркоман: \n — Чем сегодня кормите? \n Офицaнт, открывaя меню: \n — Один момент \n — Тогдa двa тюбикa """)
        if answer == 2:
                print("Заходит негр в бар. На плече у него сидит попугай. Бармен спрашивает: \n — где купил? \n Попугай отвечает: \n — на рынке")
if actions == 2:
        number_one = int(input("Введи первое число "))
        number_two = int(input("Введи второе число "))
        print(number_one + number_two)
if actions == 3:
        rando_number_one = int(input("От "))
        rando_number_two = int(input("До "))
        random_result = random.randint(rando_number_one, rando_number_two)
        print(random_result)
