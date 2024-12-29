class Car:
    def __init__(self, model: str, color:str, year: int):
        self.model = model
        self.color = color
        self.year = year
    def __str__(self):
        return f"Модель {self.model}\nЦвет: {self.color}\nГод выпуска: {self.year}"
    def make_beep(self, count:int):
        return f"Автомобиль {self.model} сделал {'Бип' * count}"
    @staticmethod
    def get_auto_value(width: int, height:int, depth:int):
        return width * height * depth
car_1 = Car("BMW", "red", 2020)
car_2 = Car("Жигули", "blue", 1990)

auto_list = [car_1, car_2]

for car in auto_list:
    print(car)
    print(car.make_beep(3))
    
print(car_1.make_beep(3))
print(car_2.make_beep(5))