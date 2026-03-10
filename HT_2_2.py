#Дана строка 'rythm (rough rush shake) than’.
#'Программа выводит только ту часть строки,)
#которая НЕ в скобочках.

string = str("rythm (rough rush shake) than")
first_bracket = string.find("(")
second_bracket = string.find(")")
print(string[:first_bracket]+string[second_bracket+1:])