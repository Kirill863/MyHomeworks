# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
# Измените элемент "milk" на "almond milk".
# Создайте срез, содержащий первые два элемента списка.
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
# Выведите список покупок, срез и вложенный список.
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]

# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
shopping_list = ['bread', 'milk', 'eggs']
# Измените элемент "milk" на "almond milk".
shopping_list[1] = 'almond milk'
# Создайте срез, содержащий первые два элемента списка.
slice_shopping_list = shopping_list[0:2]  # включается индекс 0 и 1
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
detailed_shopping_list = [
    ['bread', 1.5],
    ['almond milk', 3.0],
    ['eggs', 2.0],
]
# Выведите список покупок, срез и вложенный список.
print(shopping_list)
print(slice_shopping_list)
print(detailed_shopping_list)


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
student_list = ["Alice", "Bob", "Charlie", "David"]
# Измените имя второго студента на "Eve".
student_list[1] = "Eve"
# Создайте срез, содержащий студентов: "Bob", "Charlie".
student_list[1:4]
# Создайте вложенный список, где каждый студент имеет список своих оценок.
student_list_mark = [["Alice" , 5], ["Bob",3], ["Charlie",5], ["David",4]]
# Выведите список студентов, срез и вложенный список.
print(student_list)
print(student_list[1:3])
print(student_list_mark)
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат: [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]



# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
tasks = ["task1", "task2", "task3", "task4"]
# Измените третью задачу на "task3 updated".
tasks[2] = "task3 updated"
# Создайте срез, содержащий последние две задачи.
last_tasks = tasks[2:4]
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
detailed_tasks = [["task1", True], ["task2", False], ["task3", True], ["task4", False]]
# Выведите список задач, срез и вложенный список.
print(tasks)
print(last_tasks)
print(detailed_tasks)
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат: [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]
