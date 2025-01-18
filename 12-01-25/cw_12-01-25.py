import requests
from plyer import notification
# Просто сделаем запрос без функций
 
# CITY = "Усть-Каменогорск"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
# UNITS = "metric"
# LANGUAGE = "ru"
 
# url = fr'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}&lang={LANGUAGE}'
 
# response = requests.get(url) # Сделали запрос и получили объект ответа
# print(response.status_code) # Получили статус ответа
# print(response.json()) # Получили объект Python из JSON
 
 
# Получим описание и температуру, и ощущается как
# weather_dict = response.json()
 
class WeatherRequestError(Exception):
    pass

class WeatherRequest:
    def __init__(self, api_key: str, units:str = "metric", language: str = "ru"):
        self.api_key = api_key
        self.units = units
        self.language = language
        self.__url = ""
        self.__response: dict = {}

    def __get_request_url(self, city:str):
        self.__url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={self.units}&lang={self.language}'
    
    def get_weather(self, city: str):

        """ 
        Метод формирует запрос URL и делает запрос к погодному API
        param city - название города
        """
        
        self.__get_request_url(city)
        response = requests.get(self.__url)
        self.__response = response.json()
    
    def get_clear_wheather_data(self, city: str):
        self.get_weather(city)

        result_dict = {}

        result_dict["temp"] = self.__response["main"]["temp"]
        result_dict["feels_like"] = self.__response["main"]["feels_like"]
        result_dict["description"] = self.__response["weather"][0]["description"]

        return result_dict
    
    def get_weather_string(self, waether_dict: dict):
        temp = waether_dict["temp"]
        feels_like = waether_dict["feels_like"]
        description = waether_dict["description"]

        return f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'

    def __call__(self, city: str):
        waether_dict = self.get_clear_wheather_data(city)
        return self.get_weather_string(waether_dict)
    
weather = WeatherRequest(API_KEY)
result = weather("Москва")
# print(result)
        
class Notification:
    @staticmethod
    def send_notification(title:str, message: str):
        notification.notify(
                title=title,
                message = message,
                app_name="Погода",
                app_icon=None,
                timeout=60,
                toast=True,
                )
    
    def __call__(self, title:str, message:str):
        self.send_notification(title, message)

class WeatherFacade:
    def __init__(self, api_key:str, units:str = "metric", language: str = "ru"):
        self.weather = WeatherRequest(api_key, units, language)
        self.notification = Notification()
    
    def __call__(self, city: str):
        weather_dict = self.weather.get_clear_wheather_data(city)
        title = f"Погода в {city}"
        message = self.weather.get_weather_string(weather_dict)
        self.notification(title,message)

if __name__ == '__main__':
    weather = WeatherFacade(API_KEY)
    input_city = input("Введите название города ")
    weather(input_city)
        
# # Temp
# temp = weather_dict['main']['temp']
# # Ощущается как
# feels_like = weather_dict['main']['feels_like']
# # Описание погоды
# description = weather_dict['weather'][0]['description']
 
# print(f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')
 
# # Уведомление
# notification.notify(
#     title=f"Погода в {CITY}",
#     message=f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}",
#     app_name="Погода",
#     app_icon=None,
#     timeout=60,
#     toast=True,
# )