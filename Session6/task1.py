# Задача 1. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

test_list = [ ] # Cюда вставить список
test_item = input("Введите искомую строку: ")

def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):
         if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1

print(f" Ответ: {check_list(test_list, test_item)}")

#  Второй вариант решения задачи, для правильной работы открепить комментирование списка и закомментить первый вариант решения

my_list, find = ["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"
# my_list, find = ["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"
# my_list, find = ["123", "234", 123, "567"], "123"
# my_list, find = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"

pos = -1 if my_list.count(find) < 2 else list(filter(lambda x: x[1] == find, enumerate(my_list)))[1][0]
print(f'позиция второго вхождения "{find}" -> {pos}')

def find_second_occurence(string_list: list[str], search_word:str) -> int:
    #for index, string in enumerate(string_list): # вариант из трех строк
    #   if string == search_word:
    #       list_indexes.append(index)

    try:
        list_indexes = [index for index, string in enumerate(string_list) if string==search_word] # вариант в одну строку
        return list_indexes[0]
    except IndexError:
        return -1