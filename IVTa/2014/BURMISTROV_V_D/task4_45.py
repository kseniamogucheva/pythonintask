# Задача 4. Вариант 45.
# Напишите программу, которая выводит имя, под которым скрывается Борис Николаевич Кампов. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.
# Burmistrov V.D.
# 17.03.2016

print("Борис Николаевич Кампов более известен, как российский журналист.")

year_of_birth = 1908 
age = 1981 - year_of_birth
birthplace = "Москва, Российская империя"
interess = "журналист"

print("Место рождения:", birthplace)
print("Год рождения:", year_of_birth)
print("Возраст при смерти: ", age)
print("Область интересов: ", interess)

input("\n\nНажмите Enter для выхода.")
