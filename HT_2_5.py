#Дана строка 'rythm rough rush shake than’.
#Программа выводит строку, в которой все
#буквы ‘h’ заменены на ‘H’, кроме первого и последнего вхождений.

string = str("rythm rough rush shake than")
first_h = string.find("h")
last_h = string.rfind("h")

central_text = string[first_h+1:last_h]

big_H_of_central_text = central_text.replace("h", "H")

result = string[:first_h+1] + big_H_of_central_text + string[last_h:]
print(result)

