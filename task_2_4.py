list1 = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
list2 = []
list3 = []

i = 0
for i in range(len(list1)):
    if type(list1[i]) == float:
        r = int(list1[i])
        kk = list1[i] - int(list1[i])
        list3.append(str(r) + " руб " + str(round(kk, 1) * 100) + " коп,")
    else:
        list3.append(str(list1[i]) + " руб "+ "00 коп,")
print(' '.join(list3))
#отсортированный по возрастанию
print(sorted(list1))
#новый отсортированный по убыванию
j = 0
for j in range(len(list1)):
    list2.append(list1[j])
a = sorted(list2)
a.reverse()
print(a)

i = 0
for i in range(5):
    print(a[i])