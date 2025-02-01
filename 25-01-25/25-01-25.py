class Duck:
    default_status = "alive"

    def __init__(self, name : str, weight : float):
        self.name = name
        self.status = self.__class__.default_status
        self.weight = weight
    def __str__(self):
        return f"Утка {self.name} - {self.status}"
    
    
    def __call__(self, cooking_type : str):
        self.status = cooking_type
        print(f"Утка {self.name} готовоться к {cooking_type}")
    def __len__(self):
        return int(self.weight)
    def __bool__(self):
        return self.status != self.__class__.default_status

duck1 = Duck("Дональд", 3.8)
duck2 = Duck("Марго", 4.0)

ducks = [duck1 , duck2]

[print(duck) for duck in ducks]
[print(len(duck)) for duck in ducks]

sorted_ducks = sorted(ducks, key=len)
print(sorted_ducks)

duck1("жарить на вертеле")

if duck1:
    print("Утка готова", duck1.status)
else:
    print("Утка не готова", duck2.status)
