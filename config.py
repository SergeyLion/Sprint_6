from selenium import webdriver


class StoreConfig:
    URL_YA_SCOOTER = "https://qa-scooter.praktikum-services.ru/" #Ссылка на приложение магазина "Яндекс Самокат"
    URL_DZEN = "https://dzen.ru/" #Ссылка на страницу дзен, нужна для проверки нахождения
    TIMEOUT = 10 # Тайм-аут ожидания элемента страницы в секундах