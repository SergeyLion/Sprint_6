import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import StoreConfig as Sc



class BasePage: #Класс с базовыми методами

    def __init__(self, driver):
        self.driver = driver

    # Метод ждущий загрузки элемента по локатору
    def wait_for_load(self, locator):
        WebDriverWait(self.driver, Sc.TIMEOUT).until(expected_conditions.visibility_of_element_located(locator))

    # Метод ждущий по локатору когда элемент станет кликабельным
    def wait_for_click(self, locator):
        WebDriverWait(self.driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(locator))

    # Метод скроллит страницу к элементу
    @allure.step('Скроллит страницу к {locator}')
    def scroll_to_element(self, locator):
        self.wait_for_load(locator)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Метод проверяющий видимость элемента на странице, возвращает True если элемент отображается
    @allure.step('Проверяем видимость элемента {locator}')
    def check_is_displayed(self, locator):
        self.wait_for_load(locator)
        result = self.driver.find_element(*locator).is_displayed()
        return result

    # Метод нажимающий на элемент
    @allure.step('Нажимаем на элемент {locator}')
    def click_element(self, locator):
        self.wait_for_click(locator)
        self.driver.find_element(*locator).click()

    # Метод для ввода текста в поле ввода
    @allure.step('Вводим текст {set_data} в поле ввода {locator}')
    def set_input(self, locator, set_data):
        self.wait_for_load(locator)
        self.driver.find_element(*locator).send_keys(set_data)

    # Метод сравнивает Ожидаем URL(expect_url) c Фактическим URL(actual_url), если совпадает возвращает True
    # Метод так же принимает Локатор, для ожидания загрузки страницы
    @allure.step('Сравниваем URL текущей страницы с ожидаемой {expect_url}')
    def check_current_url(self, expect_url, locator):
        self.wait_for_load(locator)
        actual_url = self.driver.current_url
        return actual_url == expect_url




