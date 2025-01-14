import allure
import pytest

from config import StoreConfig as Sc
from conftest import driver
from locators.home_page_locators import QuestionLocators as Ql, HomeRoadMap as Hrm
from locators.base_page_locators import HeaderLocators as Hl
from locators.order_page_locators import OrderForm as Of
from pages.base_page import BasePage


class TestQuestion:

    @pytest.mark.parametrize(
        'question, answer, title_question',
        [
            [Ql.QUESTION_PRICE, Ql.ANSWER_PRICE, "Сколько это стоит? И как оплатить?"],
            [Ql.QUESTION_RENT_MULTIPLE_SCOOTERS, Ql.ANSWER_RENT_MULTIPLE_SCOOTERS, "Хочу сразу несколько самокатов! Так можно?"],
            [Ql.QUESTION_RENT_TIME_CALCULATED, Ql.ANSWER_RENT_TIME_CALCULATED, "Как рассчитывается время аренды?"],
            [Ql.QUESTION_ORDER_SCOOTER_TODAY, Ql.ANSWER_ORDER_SCOOTER_TODAY, "Можно ли заказать самокат прямо на сегодня?"],
            [Ql.QUESTION_EXTEND_ORDER, Ql.ANSWER_EXTEND_ORDER, "Можно ли продлить заказ или вернуть самокат раньше?"],
            [Ql.QUESTION_DELIVER_CHARGER, Ql.ANSWER_DELIVER_CHARGER, "Вы привозите зарядку вместе с самокатом?"],
            [Ql.QUESTION_CANCEL_ORDER, Ql.ANSWER_CANCEL_ORDER, "Можно ли отменить заказ?"],
            [Ql.QUESTION_DELIVER_OUTSIDE_MKAD, Ql.ANSWER_DELIVER_OUTSIDE_MKAD, "Я живу за МКАДом, привезёте?"]
        ]
    )
    @allure.title('Проверки раскрытия ответа на вопрос "{title_question}"')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question(self, question,answer, title_question, driver): #Проверки раскрытия ответа на вопрос
        #Открытие страницы магазина
        driver.get(Sc.URL_YA_SCOOTER)

        #Создаем объект класса базовой страницы
        base_page = BasePage(driver)

        #Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Нажатие на раскрывающийся список
        base_page.click_element(question)

        #Проверяем видимость ответа на вопрос
        assert base_page.check_is_displayed(answer), f'Ответ на вопрос "{title_question}" не отображается на странице'



class TestButtonOrder:


    @allure.title('Проверка кнопки "Заказать" в хедере страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в хедере, ждем видимости кнопку "Далее"  и проверяем фактическую страницу с ожидаемой')
    def test_button_header_order(self, driver): #Проверка кнопки "Заказать" в хедере страницы
        # Открытие страницы магазина
        driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(driver)

        #Нажимаем на кнопку "Заказать"
        base_page.click_element(Hl.BUTTON_HEADER_ORDER)

        #Проверяем нахождение на страницы "Заказа"
        assert base_page.check_current_url(Sc.URL_YA_SCOOTER_ORDER, Of.BUTTON_NEXT)

    @allure.title('Проверка кнопки "Заказать" на домашней страницы')
    @allure.description('Нажимаем на кнопку "Заказать" на домашней странице, ждем видимости кнопку "Далее"  и проверяем фактическую страницу с ожидаемой')
    def test_button_home_order(self, driver): #Проверка кнопки "Заказать" на домашней страницы
        # Открытие страницы магазина
        driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(driver)

        #Скролим страницу к кнопке "Заказать"
        base_page.scroll_to_element(Hrm.BUTTON_HOME_ORDER)

        #Нажимаем на кнопку "Заказать"
        base_page.click_element(Hrm.BUTTON_HOME_ORDER)

        #Проверяем нахождение на страницы "Заказа"
        assert base_page.check_current_url(Sc.URL_YA_SCOOTER_ORDER, Of.BUTTON_NEXT)

