# class Animal:
#     def __init__(self, name: str):
#         self._name = name
#         print("Иницилизация животного")
#     def voice(self):
#         return "Животное издает звук" 
#     def __str__(self):
#         return f"Животное по имени {self._name}"
        

# class Dog(Animal):
#     def __init__(self, name: str, breed: str):
#         # Animal.__init__(self, name)
#         super().__init__(name)
#         self.breed = breed
#         print("Иницилизация собаки")
#     def voice(self):
#         # animal_voice = Animal.voice(self)
#         animal_voice = super().voice()
#         animal_voice += " Гав"
#         return animal_voice

# dog = Dog("Шарик", "Дворняга")
# print(dog)
# print(type(dog))

# print(dog.voice())

from abc import ABC, abstractmethod

class AbstractDocument(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def append(self):
        pass
    @abstractmethod
    def write(self):
        pass

class MarkdownDocument(AbstractDocument):
    def __init__(self, file_path: str):
        super().__init__(file_path)
    
    def open(self):
        pass
    
    def read(self):
        pass
    
    def append(self):
        pass
    
    def write(self):
        pass
md_file = MarkdownDocument("file.md")