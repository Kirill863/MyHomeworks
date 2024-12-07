
time = int(input("Введите текущее время (часы от 0 до 23): "))


if time < 0 or time > 23:
    print("Пожалуйста, введите корректное время (от 0 до 23).")
else:

    if 5 <= time < 12:
        greeting = "Доброе утро!"
    elif 12 <= time < 18:
        greeting = "Добрый день!"
    elif 18 <= time < 23:
        greeting = "Добрый вечер!"
    else:
        greeting = "Доброй ночи!"


    print(greeting)
