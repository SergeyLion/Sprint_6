import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderForm as Of
from selenium.webdriver.common.by import By
import time

class OrderPage(BasePage):

    # Метод для заполнения формы заказа "Для кого?"
    @allure.step('Заполняем форму заказа "Для кого?"')
    def set_form_order_for_whom(self, data_whom_order):
        self.set_input(Of.INPUT_NAME, data_whom_order["name"])
        self.set_input(Of.INPUT_SURNAME, data_whom_order["surname"])
        self.set_input(Of.INPUT_ADDRESS, data_whom_order["address"])
        self.set_input(Of.INPUT_METRO, data_whom_order["metro"])
        time.sleep(1)
        self.click_element(Of.SELECT_METRO)
        self.set_input(Of.INPUT_PHONE, data_whom_order["phone"])
        self.click_element(Of.BUTTON_NEXT)

    # Метод для выбора даты в Календаре, переключает на следующий месяц и выбирает дату из календаря
    # На вход принимает числа в формате 01-31
    @allure.step('Выбираем дату {date} из следующего месяца')
    def set_date_picker(self, date):
        self.click_element(Of.INPUT_DATA_DELIVERY)
        self.click_element(Of.DATE_PICKER_NEXT_MONTH)
        date_picker_locator = (By.CSS_SELECTOR, f"div.react-datepicker__day--0{date}") # Локатор для дат в календаре
        self.click_element(date_picker_locator)

    # Метод для выбора срока аренды, на вход принимает числа от 1 до 7
    @allure.step('Выбираем период аренды, {rent_days} дней')
    def set_period_rent(self, rent_days):
        self.click_element(Of.DROPDOWN_PERIOD_RENT)
        rent_days_locator = (By.XPATH, f"//div[@class='Dropdown-option'][{rent_days}]") # Локатор селектов в выпадающем списке срок аренды
        self.click_element(rent_days_locator)

    # Метод для выбора самоката, на вход принимает grey и black
    @allure.step('Выбираем цвет самоката {color}')
    def set_color_scooter(self, color):
        check_color_scooter_locator = (By.XPATH, f"//input[@id='{color}']")  # Локатор для чекбокса цвета самоката в форме заказа
        self.click_element(check_color_scooter_locator)

    # Метод для заполнения формы заказа "Об аренде"
    @allure.step('Заполняем форму заказа "Об аренде"')
    def set_form_order_about_rent(self, rental_details):
        self.set_date_picker(rental_details["data_rent"])
        self.set_period_rent(rental_details["rent_days"])
        self.set_color_scooter(rental_details["color"])
        self.set_input(Of.INPUT_COMMENT, rental_details["comment"])
        self.click_element(Of.BUTTON_FORM_RENT_ORDER)

