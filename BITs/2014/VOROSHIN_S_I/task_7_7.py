#Задача №7, Вариант 7
#Компьютер загадывает имя одного из двух сооснавателей Google, а игрок угадывает. 
#Если он угадывает, то получает баллы. Если не угадывает, то его баллы уменьшаются.

#Ворошин С.И.
#21.03.2016

import random
osnavateli=('Ларри Пейдж','Сергей Брин')
osnavatel=random.randint(0,1)
rand=osnavateli[osnavatel]
Ball=100
print("Я загадал одного из оснавателей Google")
print (rand)
otvet=0
while (otvet)!=(rand):
	otvet=input("Введите одного из основателей:")
	if (otvet)!=(rand):
		print ("Вы не угадали. Попробуйте снова.")
		Ball/=2
	elif (otvet)==(rand):
		print ("Вы угадали.")
		print ("Ваши баллы:"+str(Ball))
		break

input("Нажмите Enter для выхода.")