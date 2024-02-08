import csv
#открыли файл для чтения
with open ('students.csv', encoding = 'utf8') as file:
    reader = csv.reader(file, delimiter = ',')
    answer = list(reader)[1:]


    for id, name, titleProject_id, _class, score in answer:
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")
            break


    #считаем сумму оценко и кол-во учеников по каждому классу
    count_class = {}
    summ_class = {}
    for el in answer:
        count_class[el[-2]] = count_class.get(el[-2], 0) + 1
        summ_class[el[-2]] = summ_class.get(el[-2], 0) + (int(el[-1]) if el[-1] != 'None' else 0)

    #заменяем в записях None на среднее значение
    for el in answer:
        if el[-1] == 'None':
            el[-1] = round(summ_class[el[-2]] / count_class[el[-2]], 3)

#сохранить результат в новый файл
with open ('students_new.csv', 'w', encoding = 'utf8', newline = '') as file:
    w = csv.writer (file, delimiter=',')
    w.writerow(['id', 'name', 'titleProject_id', 'class', 'score'])
    w.writerows(answer)

