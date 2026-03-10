#Дана строка 'rythm rough rush shake than’. Программа выводит строку, в которой
#последовательность символов между первым и последним появлением буквы ‘h’
#повернута в противоположном порядке

string = "rythm rough rush shake than"

first_h = string.find("h")
last_h = string.rfind("h")

middle_text = string[first_h+1:last_h]
reversed_text = middle_text[::-1]
print(reversed_text)