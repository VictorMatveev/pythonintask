# Задача 4. Вариант 9.
# Напишите программу, которая выводит имя, под которым скрывается Михаил Николаевич Румянцев. 
#Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). 
#Для хранения всех необходимых данных требуется использовать переменные. 
#После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Lungu R.U.
# 11.04.2017

print("Румянцев, Михаил Николаевич более известен, как Советский артист цирка Карандаш.")

year_of_birth = 1901 
age = 1983 - year_of_birth
birthplace = "Санкт-Петербург, Россия"
interess = "Артист цирка"

print("Место рождения:", birthplace)
print("Год рождения:", year_of_birth)
print("Возраст: ", age)
print("Область интересов: ", interess)

input("\n\nНажмите Enter для выхода.")



