# Задача 3. Вариант 15.
# Напишите программу, которая выводит имя "Норма Бейкер", и запрашивает его псевдонимПосле вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Костарев А. И.
# 29.02.2015
print ('Герой нашей сегоднешней программы - Норма Бейкер')
psev=input("Под каким же именем мы знаем этого человека? Ваш ответ: ")
if (psev)==("Мерлин Монро"):
		print ("Всё верно: Норма Бейкер - "+psev)
else:
		print ("Вы ошиблись, это не его псевдоним.")
input("Press Enter to close")
