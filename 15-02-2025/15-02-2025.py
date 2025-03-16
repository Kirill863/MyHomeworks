"""
15/02/2025
Тема: Генератры и Итераторы
"""

string = "Банан"

my_list = ["банан", "яблоко", "апельсин"]

"""
Служебные объекты - генераторы dict.keys()
dict.values()
dict.itrm()
range()
map()
filter()
"""
min_value = 0
max_value = 1000000

range_nums = range(min_value, max_value)

# обработка фильтром

even_nums = filter(lambda x: x % 2 == 0, range_nums)

#  обработка МАР

string_nums = map(lambda x: str(x) + " число", even_nums)

STOP_ITEM = "1000 число"

SEARCH_STRING = "92"

from typing import Any, Generator

def my_generator(start: int, stop: int) -> Generator[int]:
    for i in range(start, stop):
        yield i 

gen = my_generator(0, 2)

# print(next(gen))
# print(next(gen))
# print(next(gen))

def advanced_generator(start: int, stop: int) -> Generator[int, str, float]:
    current = start
    while current < stop:
        command = yield current

        if command == "double":
            current *= 2
        elif command == "square":
            current **= 2
        elif command == "cube":
            current **= 3
        else:
            current += 1
    return current

gen = advanced_generator(0, 100)
gen.send("double")
print(next(gen))
print(next(gen))
gen.send("cube")

from random import choice
from typing import Generator

fruit_list = ["яблоко", 'банан', 'груша', 'киви', 'мандарин', 'персик', 'грейпфрут', 'ананас']

class CoctailGenerator:
    def __init__(self, products: list[str]):
        self.products = products
    def __iter__(self):
        return self
    def __next__(self):
        if not self.products:
            raise StopIteration
        ftuit = choice(self.products)
        self.products.remove(fruit)
        return f"{fruit.title()} использован"

coctail_gen = CoctailGenerator(fruit_list)

for coctail