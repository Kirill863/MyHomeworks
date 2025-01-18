class Employee:
    def __init__(self, name:str, age: int, salary:int) -> None:
        self.name = name
        self._age = age
        self.__salary = salary
        self.__threshold_percent_salary: int = 50
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Заплата должна быть числом")
        if value < 0:
            raise ValueError("Зарпплата не может быть меньше 0")
                # Проверим чтобы зарплата не колебалась более чем на __threshold_percent_salary
        if abs(self.__salary - value) > self.__salary * self.__threshold_percent_salary / 100:
            raise ValueError(f"Зарплата не может колебаться более чем на 50%")
        
        self.__salary = value

manager = Employee("Владимир", 30, 100000)
print(manager.salary)

manager.salary = 120000
print(manager.salary)

manager.salary = 200000
print(manager.salary)


