def say_hello(name: str, age: int) -> None:
    """
    Функция приветсвия.
    :param name: Имя пользователя
    :param age: Возраст пользователя
    """

    print(f'Привет, {name.title()}! Тебе {age} лет.')

say_hello('Алексей', 30)

message: None = say_hello('Алексей', 34)

def is_palindrome(unit: str) -> bool:
    """
    Функция проверки на паллиндром
    :param unit: проверяемая фаза - строка
    """
    unit = unit.lower()
    """
    приведение к нижнему региструФ
    """
    return unit == unit[::-1]

print(is_palindrome("ABBA"))
print(is_palindrome("AbAb"))