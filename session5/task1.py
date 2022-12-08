txt = input("Введите текст через пробел:\n")
find_txt = input("Введите текст для удаления:\n")
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')