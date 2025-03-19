"""
Пример паттерна наблюдатель
"""
from abc import ABC, abstractmethod

class AbstractMarketObserver(ABC):
    @abstractmethod
    def update(self, data: dict) -> None:
        pass

class NotifyMarketObserver(AbstractMarketObserver):
    def update(self, data: dict)-> None:
        BTC = data.get("BTC", 0)
        ETH = data.get("ETH", 0)

        if BTC > 100000:
            print("BTC подорожал более 100000")
        
        if ETH > 5000:
            print("ETH подорожал более 5000")

class TradeMarketObserver(AbstractMarketObserver):
    def update(self, data: dict) -> None:
        TON = data.get("TON", 0)
        LTC = data.get("LTC" , 0)

        if TON > 5:
            print("Дурова выпустили из тюрьмы, TON вырос выше 5 раз, продаем!")
        if LTC > 100:
            print("LTC вырос выше 100 - покупать")

class Market:
    def __init__(self, api_key: str)-> None:
        self.api_key = api_key
        self.observers = []
        self.data = {}
    
    def add_observer(self, observer: AbstractMarketObserver)-> None:
        self.observers.append(observer)
    
    def remove_observer(self, observer: AbstractMarketObserver)-> None:
        self.observers.remove(observer)

    def _notify_observers(self, new_data: dict) -> None:
        for observer in self.observers:
            observer.update(new_data)
    
    def set_data(self, new_data: dict) -> None:
        self.data.update(new_data)
        self._notify_observers(new_data)

if __name__ == "__main__":
    market = Market(api_key="123")

    notify_observer = NotifyMarketObserver()
    trade_observer = TradeMarketObserver()

    market.add_observer(notify_observer)
    market.add_observer(trade_observer)

    market.set_data({"NOT":100})
    market.set_data({"TON":10, "LTC":200})
    market.set_data({"BTC":100000, "ETH":50000})