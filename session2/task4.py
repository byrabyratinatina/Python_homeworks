people = int(input('Количество человек в кругу: '))
count = int(input('Какое число счета (для выбывания)? '))
list_people = list(range(1, people + 1))
out_ind = 0 
for i in range(people - 1):
    start_ind = out_ind % len(list_people)    
    out_ind = (start_ind + count- 1) % len(list_people)
    list_people.remove(list_people[out_ind])
print('Остался человек под номером', list_people[0])


people_list[:count]
people_list[count:]
