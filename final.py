note = []

username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате 'день.месяц.год': ")
issue_date = input("Введите дату истечения заметки в формате 'день.месяц.год': ")
data = [username, content, status, created_date, issue_date]
note.append(data)

title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
titles = [title1, title2, title3]
note.append(titles)

print(note)
















