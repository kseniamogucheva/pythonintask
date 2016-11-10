#Задача 8. Вариант 16.
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. 
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. 
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку..

#Mogucheva K.S.
#13.10.2016

print ("Добро пожаловать в игру Анаграммы!!!" )
print ("Надо переставить буквы так, чтобы получилось осмысленное слово." )

import random
score = 10
words = ("клавиатура", "процессор", "мышка")
word = random.choice(words)
dlina = len(word)
print ("В слове", dlina, " букв." )
print ("Вот анаграмма:" )
anagrama = list(word)
random.shuffle(anagrama)
i = 0
print(anagrama)
answer = ""
while(answer!=word):
	print("Вы назовете слово?(да/нет)")
	answer = str(input())
	if (answer == str("да")or answer == str("Да") or answer == str("ДА")):
		print("Ответ: ")
		answer = str(input())
		if (answer == word):
			if (score < 0):
				score == 0
			print("Верно! Ваш счёт: ", str(score))
	else:
		print("Подсказка(да/нет)")
		answer = str(input())
		if (answer == str("да")or answer == str("Да") or answer == str("ДА")):
			print("Вы использовали подсказку, но у вас сгорели очки.", i+1, "буква: ", word[i])
			score -= 2
		else:
			print("До свидания! Заходи ещё!")
			break
input ("Нажмите Enter для выхода.")