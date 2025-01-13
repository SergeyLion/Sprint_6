import allure

from config import StoreConfig as Sc
from conftest import setup_class, teardown_class
from locators.home_page_locators import QuestionLocators as Ql, HomeRoadMap as Hrm
from locators.base_page_locators import HeaderLocators as Hl
from locators.order_page_locators import OrderForm as Of
from pages.base_page import BasePage


class TestQuestion:

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = setup_class()

    @allure.title('Проверки раскрытия ответа на вопрос "Сколько это стоит? И как оплатить?')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_price(self): #Проверки раскрытия ответа на вопрос "Сколько это стоит? И как оплатить?"
        #Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        #Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        #Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Нажатие на раскрывающийся список "Сколько это стоит? И как оплатить?"
        base_page.click_element(Ql.QUESTION_PRICE)

        #Проверяем видимость ответа на вопрос "Сколько это стоит? И как оплатить?"
        assert base_page.check_is_displayed(Ql.ANSWER_PRICE)

    @allure.title('Проверки раскрытия ответа на вопрос "Проверки раскрытия ответа на вопрос "Хочу сразу несколько самокатов! Так можно?')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_rent_multiple_scooters(self): #Проверки раскрытия ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"
        #Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        #Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        #Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)


        # Нажатие на раскрывающийся список "Хочу сразу несколько самокатов! Так можно?"
        base_page.click_element(Ql.QUESTION_RENT_MULTIPLE_SCOOTERS)

        #Проверяем видимость ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"
        assert base_page.check_is_displayed(Ql.ANSWER_RENT_MULTIPLE_SCOOTERS)

    @allure.title('#Проверки раскрытия ответа на вопрос "Как рассчитывается время аренды?"')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_time_calculated(self): #Проверки раскрытия ответа на вопрос "Как рассчитывается время аренды?"
        #Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        #Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        #Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)


        # Нажатие на раскрывающийся список "Как рассчитывается время аренды?"
        base_page.click_element(Ql.QUESTION_RENT_TIME_CALCULATED)

        #Проверяем видимость ответа на вопрос "Как рассчитывается время аренды?"
        assert base_page.check_is_displayed(Ql.ANSWER_RENT_TIME_CALCULATED)

    @allure.title('Проверки раскрытия ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_order_scooter_today(self): #Проверки раскрытия ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"
        # Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        # Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Нажатие на раскрывающийся список "Можно ли заказать самокат прямо на сегодня?"
        base_page.click_element(Ql.QUESTION_ORDER_SCOOTER_TODAY)

        # Проверяем видимость ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"
        assert base_page.check_is_displayed(Ql.ANSWER_ORDER_SCOOTER_TODAY)

    @allure.title('Проверки раскрытия ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_extend_order(self): #Проверки раскрытия ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
        # Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        # Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Нажатие на раскрывающийся список "Можно ли продлить заказ или вернуть самокат раньше?"
        base_page.click_element(Ql.QUESTION_EXTEND_ORDER)

        # Проверяем видимость ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
        assert base_page.check_is_displayed(Ql.ANSWER_EXTEND_ORDER)

    @allure.title('Проверки раскрытия ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_deliver_charger(self): #Проверки раскрытия ответа на вопрос "Вы привозите зарядку вместе с самокатом?"
        # Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        # Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Нажатие на раскрывающийся список "Вы привозите зарядку вместе с самокатом?"
        base_page.click_element(Ql.QUESTION_DELIVER_CHARGER)

        # Проверяем видимость ответа на вопрос "Вы привозите зарядку вместе с самокатом?"
        assert base_page.check_is_displayed(Ql.ANSWER_DELIVER_CHARGER)

    @allure.title('Проверки раскрытия ответа на вопрос "Можно ли отменить заказ?"')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_answer_cancel_order(self): #Проверки раскрытия ответа на вопрос "Можно ли отменить заказ?"
        # Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        # Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Нажатие на раскрывающийся список "Можно ли отменить заказ?"
        base_page.click_element(Ql.QUESTION_CANCEL_ORDER)

        # Проверяем видимость ответа на вопрос "Можно ли отменить заказ?"
        assert base_page.check_is_displayed(Ql.ANSWER_CANCEL_ORDER)

    @allure.title('Проверки раскрытия ответа на вопрос "Я живу за МКАДом, привезёте?"')
    @allure.description('Нажимаем на вопрос и проверяем видимость ответа, элемента accordion__panel')
    def test_question_deliver_outside_mkad(self): #Проверки раскрытия ответа на вопрос "Я живу за МКАДом, привезёте?"
        # Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        # Скроллим страницу до последнего элемента
        base_page.scroll_to_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Нажатие на раскрывающийся список "Я живу за МКАДом, привезёте?"
        base_page.click_element(Ql.QUESTION_DELIVER_OUTSIDE_MKAD)

        # Проверяем видимость ответа на вопрос "Я живу за МКАДом, привезёте?"
        assert base_page.check_is_displayed(Ql.ANSWER_DELIVER_OUTSIDE_MKAD)

    @classmethod
    def teardown_class(cls):
        # Закрываем браузер
        teardown_class(cls)


class TestButtonOrder:

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = setup_class()

    @allure.title('Проверка кнопки "Заказать" в хедере страницы')
    @allure.description('Нажимаем на кнопку "Заказать" в хедере, ждем видимости кнопку "Далее"  и проверяем фактическую страницу с ожидаемой')
    def test_button_header_order(self): #Проверка кнопки "Заказать" в хедере страницы
        # Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        #Нажимаем на кнопку "Заказать"
        base_page.click_element(Hl.BUTTON_HEADER_ORDER)

        #Проверяем нахождение на страницы "Заказа" https://qa-scooter.praktikum-services.ru/order
        assert base_page.check_current_url("https://qa-scooter.praktikum-services.ru/order", Of.BUTTON_NEXT)

    @allure.title('Проверка кнопки "Заказать" на домашней страницы')
    @allure.description('Нажимаем на кнопку "Заказать" на домашней странице, ждем видимости кнопку "Далее"  и проверяем фактическую страницу с ожидаемой')
    def test_button_home_order(self): #Проверка кнопки "Заказать" на домашней страницы
        # Открытие страницы магазина
        self.driver.get(Sc.URL_YA_SCOOTER)

        # Создаем объект класса базовой страницы
        base_page = BasePage(self.driver)

        #Скролим страницу к кнопке "Заказать"
        base_page.scroll_to_element(Hrm.BUTTON_HOME_ORDER)

        #Нажимаем на кнопку "Заказать"
        base_page.click_element(Hrm.BUTTON_HOME_ORDER)

        #Проверяем нахождение на страницы "Заказа" https://qa-scooter.praktikum-services.ru/order
        assert base_page.check_current_url("https://qa-scooter.praktikum-services.ru/order", Of.BUTTON_NEXT)




    @classmethod
    def teardown_class(cls):
        # Закрываем браузер
        teardown_class(cls)