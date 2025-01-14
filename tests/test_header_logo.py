import allure
from config import StoreConfig as Sc
from conftest import setup_class, teardown_class
from locators.base_page_locators import HeaderLocators as Hl
from pages.base_page import BasePage


class TestHeader:


    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = setup_class()

    @allure.title('Проверка открытия страницы "Дзен" по нажатию на логотип "Яндекс"')
    @allure.description('На странице Дзен ждем загрузки кнопки "Найти" и проверяем фактическую страницу с ожидаемой')
    @allure.link(Sc.URL_DZEN, name='Ожидаемая страница')
    def test_yandex_logo_redirect(self): #Проверка открытия страницы "Дзен" по нажатию на логотип "Яндекс"

        #Открываем домашнюю страницу "Яндекс Самокат"
        self.driver.get(Sc.URL_YA_SCOOTER)

        #Создаем объект от Базового класса
        base_page = BasePage(self.driver)

        #Нажимаем на логотип "Яндекс"
        base_page.click_element(Hl.LINK_LOGO_YANDEX)

        #Переключаемся на открывшеюся страницу
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

        #Проверяем адрес текущей страницы
        assert base_page.check_current_url(Sc.URL_DZEN, Hl.BUTTON_SEARCH_DZEN)

    @allure.title('Проверка открытия домашней страницы по нажатию на логотип "Самокат"')
    @allure.description('На Домашней странице ждем загрузки кнопки "Заказать" и проверяем фактическую страницу с ожидаемой')
    @allure.link(Sc.URL_YA_SCOOTER, name='Ожидаемая страница')
    def test_scooter_logo_redirect(self): #Проверка открытия домашней страницы по нажатию на логотип "Самокат"

        # Открываем домашнюю страницу "Яндекс Самокат"
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект от Базового класса
        base_page = BasePage(self.driver)

        #Нажимаем на кнопку "Заказать"
        base_page.click_element(Hl.BUTTON_HEADER_ORDER)

        #Нажимаем на логотип "Самокат"
        base_page.click_element(Hl.LINK_LOGO_SCOOTER)

        #Проверяем адрес текущей страницы
        assert base_page.check_current_url(Sc.URL_YA_SCOOTER, Hl.BUTTON_HEADER_ORDER)

    @classmethod
    def teardown_class(cls):
        # Закрываем браузер
        teardown_class(cls)







