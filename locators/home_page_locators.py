from selenium.webdriver.common.by import By


class QuestionLocators:
    TITLE_IMPORTANT_QUESTIONS = (By.XPATH, "//div[text()='Вопросы о важном']") #Заголовок "Вопросы о важном"
    QUESTION_PRICE = (By.ID, "accordion__heading-0") #Аккордеон вопроса "Сколько это стоит? И как оплатить?"
    ANSWER_PRICE = (By.ID, "accordion__panel-0") #Панель аккордеона вопроса "Сколько это стоит? И как оплатить?"
    QUESTION_RENT_MULTIPLE_SCOOTERS = (By.ID, "accordion__heading-1") #Аккордеон вопроса "Хочу сразу несколько самокатов! Так можно?"
    ANSWER_RENT_MULTIPLE_SCOOTERS = (By.ID, "accordion__panel-1") #Панель аккордеона "Хочу сразу несколько самокатов! Так можно?"
    QUESTION_RENT_TIME_CALCULATED = (By.ID, "accordion__heading-2") #Аккордеон вопроса "Как рассчитывается время аренды?"
    ANSWER_RENT_TIME_CALCULATED = (By.ID, "accordion__panel-2") #Панель аккордеона "Как рассчитывается время аренды?"
    QUESTION_ORDER_SCOOTER_TODAY = (By.ID, "accordion__heading-3") #Аккордеон вопроса "Можно ли заказать самокат прямо на сегодня?"
    ANSWER_ORDER_SCOOTER_TODAY = (By.ID, "accordion__panel-3") #Панель аккордеона "Можно ли заказать самокат прямо на сегодня?"
    QUESTION_EXTEND_ORDER = (By.ID, "accordion__heading-4") #Аккордеон вопроса "Можно ли продлить заказ или вернуть самокат раньше?"
    ANSWER_EXTEND_ORDER = (By.ID, "accordion__panel-4") #Панель аккордеона "Можно ли продлить заказ или вернуть самокат раньше?"
    QUESTION_DELIVER_CHARGER = (By.ID, "accordion__heading-5") #Аккордеон вопроса "Вы привозите зарядку вместе с самокатом?"
    ANSWER_DELIVER_CHARGER = (By.ID, "accordion__panel-5") #Панель аккордеона "Вы привозите зарядку вместе с самокатом?"
    QUESTION_CANCEL_ORDER = (By.ID, "accordion__heading-6") #Аккордеон вопроса "Можно ли отменить заказ?"
    ANSWER_CANCEL_ORDER = (By.ID, "accordion__panel-6") #Панель аккордеона "Можно ли отменить заказ?"
    QUESTION_DELIVER_OUTSIDE_MKAD = (By.ID, "accordion__heading-7") #Аккордеон вопроса "Я живу за МКАДом, привезёте?"
    ANSWER_DELIVER_OUTSIDE_MKAD = (By.ID, "accordion__panel-7") #Панель аккордеона "Я живу за МКАДом, привезёте?"

class HomeRoadMap:
    BUTTON_HOME_ORDER = (By.XPATH, "//div[contains(@class,'Home_Finish')]/button[text()='Заказать']") #Кнопка "Заказать" на домашней страницы
