﻿#Задача 9. Вариант 35.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо
#буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

#Машаева А.Ю
#29.05.2016

import random
WORDS=("Адырхаева","Лавровский","Фадеечев","Акимов","Кондратьева","Владимиров","Семеняка","Павлова")
word=random.choice(WORDS)
live=5
bukva=""
slovo=""
(chislo)=len(word)
print("Я загадала фамилию одного из народных артистов СССР ",str(chislo),"букв.")
print("У тебя " +str(live)+ " попытки угадать буквы")
while live>0:
	#print (word)
	bukva=input("Введи букву\n")
	if bukva in list(word):
		print("Да.")
		live=live-1
	else:
		print("Нет.")
		live=live-1
if live==0:
	slovo=input("Твои попытки кончились. Угадай артиста СССР")
	if slovo==word:
		print("Ты угадал народного Артиста СССР")
	else:
		print("Ты не угадал народного Артиста СССР ")
input("Нажмите Enter для выхода.")
