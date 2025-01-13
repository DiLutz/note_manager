
note = {}

note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки: ")
note["created_date"] = input("Введите дату создания заметки в формате 'день.месяц.год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день.месяц.год': ")

title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
note["titles"] = [title1, title2, title3]

print(note)
















