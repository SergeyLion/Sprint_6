from selenium import webdriver


class StoreConfig:
    URL_YA_SCOOTER = "https://qa-scooter.praktikum-services.ru/" #Ссылка на приложение магазина "Яндекс Самокат"
    URL_DZEN = "https://dzen.ru/?yredirect=true" #Ссылка на страницу дзен, нужна для проверки нахождения
    URL_YA_SCOOTER_ORDER = "https://qa-scooter.praktikum-services.ru/order" # Ссылка на страницу заказа Самоката
    TIMEOUT = 10 # Тайм-аут ожидания элемента страницы в секундах