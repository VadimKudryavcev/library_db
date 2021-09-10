from datetime import date

def group(arr):
    #Алгоритм проверяет есть ли списки повторения, и если есть, то удалаяет их
    arr_copy = []
    for a in arr:
        arr_copy.append(a[0])
    new_list = []
    i = 0
    lenght = len(arr_copy)
    while i < lenght:
        j = i + 1
        while j < lenght:
            if arr_copy[i] == arr_copy[j]:
                arr_copy.pop(j)
                lenght = len(arr_copy)
            else:
                j += 1
        new_list.append(arr_copy[i])
        lenght = len(arr_copy)
        i += 1
    return new_list

#Создание списка простейшим способом
borrow = []

borrow.append(('Mike', 20210901, None, 14)) #name (имя студента), borrow_date (дата выдачи), return_date (дата возврата), time (срок)
borrow.append(('Jack', 20210803, 20210812, 14))
borrow.append(('Mike', 20210901, 20210903, 14))
borrow.append(('Alex', 20190403, None, 14))
borrow.append(('Harry', 20190403, 20210406, 14))
borrow.append(('Jack', 20210803, 20210812, 14))
borrow.append(('Mike', 20210901, 20210903, 14))
borrow.append(('Alex', 20190403, None, 14))
borrow.append(('Harry', 20190403, 20210406, 14))
borrow.append(('Jack', 20210803, 20210812, 14))
borrow.append(('Mike', 20210901, 20210903, 14))
borrow.append(('Alex', 20190403, None, 14))
borrow.append(('Harry', 20190403, 20210406, 14))

#Вариант 1 - "злостный читатель" тот, кто много читает
print('Вариант 1 - "злостный читатель" тот, кто много читает')
borrow_copy = []
for b in borrow:
    borrow_copy.append(b[0])

#Алгоритм проверяет есть ли списки повторения, и если есть, то удалаяет их и считает их количество
student_list = []
maximum = 0
i = 0
lenght = len(borrow_copy)
while i < lenght:
    k = 1
    j = i + 1
    while j < lenght:
        if borrow_copy[i] == borrow_copy[j]:
            k += 1
            borrow_copy.pop(j)
            lenght = len(borrow_copy)
        else:
            j += 1
    if k > maximum:
        maximum = k
    student_list.append([borrow_copy[i], k])
    lenght = len(borrow_copy)
    i += 1

for student in student_list:
    if student[1] == maximum:
        print(student[0])

#Вариант 2 - "злостный читатель" тот, кто не вовремя сдал книгу
print('Вариант 2 - "злостный читатель" тот, кто не вовремя сдал книгу')
student_list = []

#Алгоритм сверяет значения разницы между датами получения и возвращения со сроком выдачи
for b in borrow:
    if b[2] != None:
        if b[2] - b[1] > b[3]:
            student_list.append(b)
new_list = group(student_list)
print(new_list)

#Вариант 3 - "злостный читатель" тот, кто не сдал книгу, хотя срок уже прошел  
print('Вариант 3 - "злостный читатель" тот, кто не сдал книгу, хотя срок уже прошел')
today = date.today()
current_date = int(today.strftime("%Y%m%d"))

student_list = []
#Алгоритм сверяет значения разницы между датами получения и нынешней со сроком выдачи
for b in borrow:
    if b[2] == None:
        if current_date - b[1] > b[3]:
            student_list.append(b)
new_list = group(student_list)
print(new_list)
