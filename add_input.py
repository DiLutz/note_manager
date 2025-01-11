
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
created_date = input("Введите дату создания заметки в формате 'день.месяц.год': ")

title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
titles = title1, title2, title3

print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголвоки заметки:", titles)
print("Описание заметки:", content)
print("Дата создания заметки:", created_date)