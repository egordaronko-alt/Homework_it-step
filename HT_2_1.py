#Дана строка 'rythm rough rush shake than’.
#Программа удаляет все буквы «а» в строке и
#подсчитывает кол-во уждаленных символов.

string = str("rythm rough rush shake than")
number_of_deleted_a = string.count("a")
string_without_a = string.replace("a",'')
print("Number of deleted 'a' is:",number_of_deleted_a,"\nString without deleted 'a' is: ",string_without_a)