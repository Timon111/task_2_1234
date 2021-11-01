list1 = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
i = 0
list2 = []
for i in range(len(list1)):
    if '+' in list1[i] or '-' in list1[i]:
        list2.append('""')
        list2.append(str(list1[i]))
        list2.append('""')
    elif list1[i].isdigit():
        list2.append('""')
        list2.append(str(list1[i]))
        list2.append('""')
    elif not list1[i].isdigit():
        list2.append(str(list1[i]))
print(list2)
