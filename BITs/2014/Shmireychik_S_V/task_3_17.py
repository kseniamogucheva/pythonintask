#Задача №3, Вариант 7
#Программа выводит имя "Симона Руссель" и запросит ее псевдоним,который пользователь напишет сам.

#Шмирейчик С.В.
#29.02.2016

print("Герой нашей сегодняшней программы - Симона Руссель")
psev=input("Под каким же именем мы знаем этого человека? Ваш ответ:")
if (psev)==("Мишель Морган"):
	print ("Все верно: Симона Руссель - "+psev)
else:
	print("Вы ошиблись, это не его псевдоним.")
input(" Нажмите Enter для выхода")