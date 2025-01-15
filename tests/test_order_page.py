import allure
import pytest
from config import StoreConfig as Sc
from conftest import driver
from locators.order_page_locators import OrderForm as Of
from locators.base_page_locators import HeaderLocators as Hl
from pages.order_page import OrderPage


class TestOrder:


    @pytest.mark.parametrize(
        'customer, rental_details',
        [
            [
                {"name":"Сергей","surname":"Львов","address":"Архивная 7, корпус 1, квартира 54","metro":"Речно ","phone":"+79231135951"},
                {"data_rent":"11","rent_days":"1","color":"black","comment":"Позвонить за 30 минут"}
            ], #Тестовые данные первого заказчика
            [
                {"name":"Алёна","surname":"Кунгурова","address":"Марата 10, квартира 21","metro":"Спорти ","phone":"+79213184745"},
                {"data_rent":"22","rent_days":"3","color":"grey","comment":"Вход во двор со стороны метро Спартак"}
            ], #Тестовые данные второго заказчика
            [
                {"name":"Антон","surname":"Петров","address":"Ленина 15, квартира 13","metro":"Шаболо ","phone":"+79062060606"},
                {"data_rent":"27","rent_days":"7","color":"black","comment":"В первой половине дня"}
            ] #Тестовые данные Третьего заказчика
        ]
    )
    @allure.title(
        'Проверка возможности забронировать самокат')
    @allure.description(
        'Заполняем формы заказа, данными заказчика и деталями заказа, проверяем появления окна успеха, в котором ждем видимость кнопки "Проверить статус"')
    def test_rent_order(self, customer, rental_details, driver): #Проверка оформления заказа
        # Открытие страницы магазина
        driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        order_page = OrderPage(driver)

        #Переходим на страницу оформления заказа
        order_page.click_element(Hl.BUTTON_HEADER_ORDER)

        #Заполняем форму "Для кого самокат"
        order_page.set_form_order_for_whom(customer)

        # Заполняем форму "Про аренду"
        order_page.set_form_order_about_rent(rental_details)

        #Подтверждения заказа в модальном окне "Хотите оформить заказ?"
        order_page.click_element(Of.BUTTON_ORDER_YES)

        #Проверка наличия модального окна "Заказ оформлен" по кнопке "Посмотреть статус"
        assert order_page.check_is_displayed(Of.BUTTON_ORDER_VIEW_STATUS)
