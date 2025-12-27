# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, c=','):
    a1 = a.split(c)
    b1 = b.split(c)
    d = set(a1).intersection(set(b1))
    return d

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group,'|'))
# TODO Провеьте работу функции с разделителем отличным от запятой