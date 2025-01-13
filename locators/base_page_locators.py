from selenium.webdriver.common.by import By


class HeaderLocators:
    BUTTON_HEADER_ORDER = (By.XPATH, "//div[contains(@class,'Header')]/button[text()='Заказать']") #Кнопка "Заказать" в хедере страницы
    LINK_LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]") #Ссылка в логотипе "Самокат"
    LINK_LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]") #Ссылка в логотипе "Яндекс"
    BUTTON_SEARCH_DZEN = (By.XPATH, "//button[text()='Найти']") #Кнопка "Найти" на странице "Дзен", нужна для ожидания полной загрузки