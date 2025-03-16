"""
Повденческие патерны
Пример паттерна стратегия, на примере анализа рынка валюты
"""
from abc import ABC, abstractmethod
class TechAnalysContext:
    def __init__(self, strategy: "AbstractStrategy") -> None:
        self.strategy = strategy
    def set_strategy(self, strategy: "AbstractStrategy") -> None:
        self.strategy = strategy
    def execute_strategy(self, message: str) -> str:
        return self.strategy.execute(message)

class AbstractStrategy(ABC):

    @abstractmethod
    def execute(self, message: str) -> str:
        pass

class StrategyAnalysOne(AbstractStrategy):
    def execute(self, message: str) -> str:
        return f"Анализ 1 :{message}"

class StrategyAnalysTwo(AbstractStrategy):
    def execute(self, message: str) -> str:
        return f"Анализ 2 :{message}"
    
user_choice = input("Введите стратегию анализа (1/2)")
try:
    int_choise = int(user_choice)
except ValueError:
    print("Введите 1 или 2 ")
    exit(1)

if int_choise == 1:
    strategy = StrategyAnalysOne()
elif int_choise == 2:
    strategy = StrategyAnalysTwo()

context = TechAnalysContext(strategy)
message = input("Введите сообщение для анализа")
result = context.execute_strategy(message)
print(result)
