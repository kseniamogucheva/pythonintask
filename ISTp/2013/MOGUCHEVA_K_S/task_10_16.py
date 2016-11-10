#Задача 10. Вариант 16.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть представлено 30 пунктов, которые можно распределить между четырьмя характеристиками: сила, здоровье, мудрость и ловкость.
#Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать из туда из характеристик, которым он решил присвоить другие значения.
#Mogucheva K.S.
#27.10.2016

choice = None
global_choice = None
power = 0
health = 0
wisdom = 0
dexterity = 0

while global_choice != 0:
 
    # Вывод актуальной таблицы после действия.
    ost_points = (30 - power - health - wisdom - dexterity)
    print("Список характеристик на данный момент: \n"
        "\t\t\t1. Сила:", power, "\n"
        "\t\t\t2. Здоровье:", health, "\n"
        "\t\t\t3. Мудрость:", wisdom, "\n"
        "\t\t\t4. Ловкость:", dexterity, "\n\n"
        "\t\t\tСвободное количество очков:", ost_points, "\n")
 
    # Первый выбор
    print("Что бы вы хотели сделать?\n"
        "\t\t\t1. Добавить очки в одну из характеристик.\n"
        "\t\t\t2. Убрать очки из характеристики.\n"
        "\t\t\t3. Закончить распределиние очков.\n")
    global_choice = int(input())
    if global_choice == 1:
        print("В какую из характеристик вы хотите добавить очки?\n"
            "\t\t\t1. Сила.\n"
            "\t\t\t2. Здоровье.\n"
            "\t\t\t3. Мудрость.\n"
            "\t\t\t4. Ловкость.\n")
        choice = int(input())
        if choice == 1:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                power += scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 2:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                health += scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 3:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                wisdom += scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 4:
            print("Сколько очков вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                dexterity += scores
            else:
                print("Недопустимое количество очков.\n")
 
    # Второй выбор
    elif global_choice == 2:
        print("Из какой характеристики вы хотите убрать очки?\n"
            "\t\t\t1. Сила.\n"
            "\t\t\t2. Здоровье.\n"
            "\t\t\t3. Мудрость.\n"
            "\t\t\t4. Ловкость.\n")
        choice = int(input())
        if choice == 1:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (power - scores) >= 0:
                power -= scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 2:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (health - scores) >= 0:
                health -= scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 3:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (wisdom - scores) >= 0:
                wisdom -= scores
            else:
                print("Недопустимое количество очков.\n")
        elif choice == 4:
            print("Сколько очков вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (dexterity - scores) >= 0:
                dexterity -= scores
            else:
                print("Недопустимое количество очков.\n")
 
    # Проверяем, все ли очки использованы.
    elif global_choice == 3:
        if ost_points == 0:
            break
        else:
            print("Используйте все очки!\n")
 
 
print("Список характеристик вашего героя теперь выглядит так: \n"
    "\t\t\t1. Сила:", power, "\n"
    "\t\t\t2. Здоровье:", health, "\n"
    "\t\t\t3. Мудрость:", wisdom, "\n"
    "\t\t\t4. Ловкость:", dexterity, "\n")
 
input("\nНажмите Enter, чтобы выйти...")