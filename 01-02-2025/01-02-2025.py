# # """
# # 01.02.2025

# # Тема: ООП Ч8. Разбор ДЗ. Погружение в Dataclasses Урок: 23

# # - Магические методы математика
# # - __add__ - сложение
# # - __sub__ - вычитание
# # - __mul__ - умножение
# # - __truediv__ - деление
# # - __floordiv__ - целочисленное деление
# # - __mod__ - остаток от деления
# # - __pow__ - возведение в степень
# # - __abs__ - модуль числа
# # - __round__ - округление
# # - __ceil__ - округление вверх
# # - __floor__ - округление вниз
# # - __int__ - преобразование в целое число
# # - __float__ - преобразование в число с плавающей точкой

# # Инплейс операции

# # - __iadd__ - +=
# # - __isub__ - -=
# # - __imul__ - *=
# # - __itruediv__ - /=
# # - __ifloordiv__ - //=

# # - __str__ - строковое представление объекта
# # - __repr__ - строковое представление объекта для разработчика


# # СРАВНЕНИЕ НА БОЛЬШЕ МЕНЬШЕ
# # - less then - __lt__ - меньше чем <
# # - great then - __gt__ - больше чем >
# # - less or equal - __le__ - меньше или равно <=
# # - great or equal - __ge__ - больше или равно >=
# # - equal - __eq__ - равно ==
# # - not equal - __ne__ - не равно !=


# # Достаточно 2 магических метода чтобы Python просчитал остальные
# # eq - равенство
# # lt - меньше чем

# # from functools import total_ordering
# # """

# # # ДАТАКЛАССЫ

# # from dataclasses import dataclass, field

# # @dataclass(order=True)
# # class MusicCompositionData:
# #     name: str = field(compare=False)
# #     author: str = field(compare=False)
# #     year: int = field(compare=False)
# #     duration: int


# # composition1 = MusicCompositionData(
# #     name="Nothing Else Matters",
# #     author="James Hetfield, Lars Ulrich",
# #     year=1991,
# #     duration=290,
# # )


# # # Создание экземпляра для песни "Nothing Else Matters" (Apocalyptica)
# # composition2 = MusicCompositionData(
# #     name="Nothing Else Matters",
# #     author="James Hetfield, Lars Ulrich (исполнение Apocalyptica)",
# #     year=1996,
# #     duration=490,  # Длительность в секундах (6 минут 30 секунд)
# # )

# # # Распечатаем
# # # print(composition1)
# # # # Repr распечатаем
# # # print(repr(composition1))
# # # MusicCompositionData(name='Nothing Else Matters', author='James Hetfield, Lars Ulrich', year=1991, duration=290)

# # print(composition1 == composition2)
# # print(composition1 < composition2)



# #PRACTICE
# """
# Сделайте 3 экземпляра датакласса MusicCompositionData
# Поместите их в список
# Попробуйте сравнить на больше меньше 2 из них
# Попробуйте применить к списку .sort() c reverse=True и без него
 
# """
# from dataclasses import dataclass, field

# @dataclass(order=True)
# class MusicCompositionData:
#     name: str = field(compare=False)
#     author: str = field(compare=False)
#     year: int = field(compare=False)
#     duration: int

# composition3 = MusicCompositionData(
#     name="Bohemian Rhapsody",
#     author="Freddie Mercury",
#     year=1975,
#     duration=355
# )

# composition4 = MusicCompositionData(
#     name="Stairway to Heaven",
#     author="Jimmy Page, Robert Plant",
#     year=1971,
#     duration=482
# )

# composition5 = MusicCompositionData(
#     name="Hotel California",
#     author="Don Felder, Glenn Frey, Don Henley",
#     year=1976,
#     duration=390
# )

# compositions_list_1 = [composition3, composition4, composition5]


# # print(compositions_list_1)
# # print(repr(composition3))
# compositions_list_1.sort
# print(compositions_list_1)
# compositions_list_1.sort(reverse=True)
# print()
# print(compositions_list_1)
# print()

# print(composition3 == composition4)
# print(composition4 < composition5)

from dataclasses import dataclass, field

# @dataclass
# class Employee:
#     name: str
#     age: int
#     position: str
#     hourly_rate: float
#     worked_hours: list = field(default_factory = list)

#     def get_salary(self):
#         return self.hourly_rate * sum(self.worked_hours)

# director = Employee(name = "Bob", age = 60, position = "Director", hourly_rate = 100)
# worker = Employee(name = "Alice", age = 30, position= "Worker", hourly_rate = 20)

# worker.worked_hours.append(8)
# worker.worked_hours.append(8)
# worker.worked_hours.append(8)

# print(worker.worked_hours)
# print(director.worked_hours)
# print(worker.get_salary())
# print(director.get_salary())

@dataclass
class Song:
    name: str
    duration: int
    duration_str: str = field(init=False)

    def __post_init__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        self.duration_str = f"Продолжительность трека {minutes}:{seconds:02d}"

    def __str__(self):
        return f"{self.name} - {self.duration_str}"

song = Song("Группа крови", 290)
print(song.duration_str)

repr_song = repr(song)
print(repr_song)

restored_song = eval(repr_song)
print(restored_song)