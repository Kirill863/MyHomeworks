"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
"""
 
# from abc import ABC, abstractmethod
 
 
# class AbstractDocument(ABC):
#     def __init__(self, file_path: str) -> None:
#         self.file_path = file_path
#         self.file = self.open()
   
#     @abstractmethod
#     def open(self):
#         pass
 
#     @abstractmethod
#     def read(self):
#         pass
 
#     @abstractmethod
#     def append(self):
#         pass
   
#     @abstractmethod
#     def write(self):
#         pass
 
#     def __str__(self) -> str:
#         return f"{self.__class__.__name__} - {self.file_path}"
 
# class TxtDocument(AbstractDocument):
#     def __init__(self, file_path: str):
#         super().__init__(file_path)
#     def open(self):
#         with open(self.file_path, "r", encoding="utf-8") as file:
#             return file.read()
#     def read(self):
#         pass
#     def append(self):
#         pass
#     def write(self):
#         pass

# class MarkdownDocument(AbstractDocument):
#     def __init__(self, file_path: str) -> None:
#         super().__init__(file_path)
 
#     def open(self):
#         pass
#     def read(self):
#         pass
#     def append(self):
#         pass
#     def write(self):
#         pass
 
 
# class PdfDocument(AbstractDocument):
#     def __init__(self, file_path: str) -> None:
#         super().__init__(file_path)
 
#     def open(self):
#         pass
#     def read(self):
#         pass
#     def append(self):
#         pass
#     def write(self):
#         pass
 
 
# # abstract = AbstractDocument() # Это не работает. Мы не можем создать экземпляр абстрактного класса
# md_file = MarkdownDocument("file.md")
# pdf_file = PdfDocument("file.pdf")
 
# print(md_file)
# print(pdf_file)

# file = "пример.txt"
# txt_file = TxtDocument(file)
# print(txt_file.file)

# class A:
#     def __init__(self, attr_a: str):
#         print("Иницилизация класса А")
#         self.attr_a = attr_a

#     def method_a(self):
#         print("Метод A")  

# class B(A):
#     def __init__(self, attr_a: str, attr_b: str):
#         super().__init__(attr_a)
#         print("Иницилизация класса В")  
#         self.attr_b = attr_b 

#     def method_b(self):
#         print("Метод B")  

# class C(B):
#     def __init__(self , attr_a: str, attr_b: str, attr_c : str):
#         super().__init__(attr_a, attr_b)
#         print("Иницилизация класса С") 
#         self.attr_c = attr_c 
    
#     def method_c(self):
#         print("Метод С")  

# c = C("A", "B", "C")
# c.method_a()
# c.method_b()
# c.method_c()






# class A:
#     def __init__(self):
#         print("Иницилизатор класса А")
        
#     def method_a(self):
#         print("Метод А")

# class B:
#     def __init__(self):
#         print("Иницилизатор класса В")
        
#     def method_a(self):
#         print("Метод А в классе В")

# class C(B,A):
#     pass

# c = C()
# c.method_a()

# print(C.mro())

# class A:
#     def __init__(self, attr_a : str):
#         self.attr_a = attr_a
#     def method_a(self):
#         print(f"Метод А: {self.attr_a}")

# class B:
#     def __init__(self, attr_b = str):
#         self.attr_b = attr_b
#     def method_b(self):
#         print(f"Метод B: {self.attr_b}")    
# class C(A,B):
#     def __init__(self, attr_a = str,attr_b = str,attr_c = str, ):
#         A.__init__(self, attr_a)
#         B.__init__(self, attr_b)
#         self.attr_c = attr_c

# Создаём миксины для различных способностей животных

class SwimMixin:

    def swim(self):

        return f"{self.__class__.__name__} животное по имени {self.name} плавает в воде"
 
class FlyMixin:

    def fly(self):

        return f"{self.__class__.__name__} животное по имени {self.name} летит по небу"
 
class RunMixin:

    def run(self):

        return f"{self.__class__.__name__} животное по имени {self.name} бежит по земле"
 
# Базовый класс животного

class Animal:

    def __init__(self, name):

        self.name = name
 
    def eat(self):

        return f"{self.name} кушает"
 
# Теперь создаём конкретных животных с нужными способностями

class Duck(Animal, SwimMixin, FlyMixin):

    def make_sound(self):

        return "Кря-кря!"
 
class Cat(Animal, RunMixin):

    def make_sound(self):

        return "Мяу!"
 
class Penguin(Animal, SwimMixin, RunMixin):

    def make_sound(self):

        return "курлык!"

 
# Создаём животных

donald = Duck(name="Дональд")

murzik = Cat(name="Мурзик")

rico = Penguin(name="Рико")
 
# Проверяем их способности

print(donald.swim())  # Выведет: Duck плавает в воде

print(donald.fly())   # Выведет: Duck летит по небу

print(murzik.run())   # Выведет: Cat бежит по земле

print(rico.swim())    # Выведет: Penguin плавает в воде

 