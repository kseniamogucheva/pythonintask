﻿# Задача 4. Вариант 14.
# Напишите программу, которая выводит имя, под которым скрывается Михаил Ефимович Фрилянд. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Моренко А.А.
# 07.03.2016

print("Мойсей Фри́длянд")
psev="Михаи́л Ефи́мович Кольцо́в"
oblinter="советский публицист и журналист, писатель, общественный деятель."
mrozh="Киев, Российская империя"
msmert="Москва, СССР"
vzhizni=1898-1940
print("Псевдоним: "+psev)
print("О личности: "+oblinter)
print("Место рождения: "+mrozh)
print("Место смерти: "+msmert)
print("Возраст: "+str(vzhizni))


input("\n\nНажмите Enter для выхода.")