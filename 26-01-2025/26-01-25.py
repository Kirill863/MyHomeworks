"""
Тема ООП. Магические методы. Математикаю Сравнение. Dataclasses
Магические методы в математике
"""

from functools import total_ordering

class MusicComposition:
    def __init__(self, name: str, author: str, year: int, duration ):
        self.name = name
        self.author = author
        self.year = year
        self.duration = duration
    
    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Автор: {self.author}\n"
            f"Год выпуска: {self.year}\n"
            f"Продолжительность: {self.duration}"
        )

    def __repr__(self):
        return f"MusicComposition(name='{self.name}', author='{self.author}', year='{self.year}', duration='{self.duration}')"
    
    def __eq__(self, other):
        if not isinstance(other, MusicComposition):
            raise TypeError("Неверный тип данных")
        return(
            self.duration == other.duration
        )
class PlayList:
    def __init__(self, name):
        self.name = name
        self.tracks: list[MusicComposition] = []
    
    def __len__(self):
        return len(self.tracks)
    
    def __str__(self):
        return f"Название плейлиста: {self.name}\n" f"Колличество треков {len(self)}"
    def __iadd__(self, other: MusicComposition):
        if not isinstance(other, MusicComposition):
            raise TypeError("неверный тип данных")
        self.tracks.append(other)
        return self
    
    def __add__(self, other: MusicComposition):
        return self.__iadd__(other)
    


composition1 = MusicComposition(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich",
    year=1991,
    duration=390
)
composition2 = MusicComposition(
    name="Nothing Else Matters",    
    author="James Hetfield, Lars Ulrich (исполнение Apocalyptica)",    
    year=1996,    
    duration=390)

playlist = PlayList(name = "Best of Metallica")

playlist += composition1
playlist = playlist + composition2

print(playlist.tracks)

compositions = [composition1, composition2]

print(compositions)
print(compositions[0])

rep = repr(composition1)

obj = eval(rep)



print(composition1 == composition2)
print(composition1 != composition2)
print(composition1 < composition2)
print(composition1 > composition2)
print(composition1 <= composition2)
print(composition1 >= composition2)