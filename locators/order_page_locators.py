from selenium.webdriver.common.by import By


class OrderForm:
    #Форма "Для кого самокат"
    INPUT_NAME = (By.XPATH, "//input[contains(@placeholder,'Имя')]") #Поле вода "Имя" в форме заказа
    INPUT_SURNAME = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]") #Поле вода "Фамилия" в форме заказа
    INPUT_ADDRESS = (By.XPATH, "//input[contains(@placeholder,'Адрес')]") #Поле вода "Адрес" в форме заказа
    INPUT_METRO = (By.XPATH, "//input[contains(@placeholder,'Станция метро')]") #Поле вода "Станция метро" в форме заказа
    SELECT_METRO = (By.XPATH, "//div[@class='select-search__select']/child::*") #Селект для выбора потомка, списка станций метро
    INPUT_PHONE = (By.XPATH, "//input[contains(@placeholder,'Телефон')]") #Поле вода "Телефон" в форме заказа
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']") #Кнопка "Далее" в форме заказа
    #Форма "Про аренду"
    INPUT_DATA_DELIVERY = (By.XPATH, "//input[contains(@placeholder,'Когда привезти самокат')]") #Поле вода "Когда привезти самокат" в форме заказа
    DATE_PICKER_NEXT_MONTH = (By.XPATH, "//button[text()='Next Month']")
    DROPDOWN_PERIOD_RENT = (By.XPATH, "//div[@class='Dropdown-control']") #Раскрывающийся список "Срок аренды" в форме заказа
    CHECK_COLOR_BLACK_SCOOTER = (By.XPATH, "//input[@id='black']") #ЧекБокс "чёрный жемчуг" в форме заказа
    CHECK_COLOR_GREY_SCOOTER = (By.XPATH, "//input[@id='grey']")  # ЧекБокс "серая безысходность" в форме заказа
    INPUT_COMMENT = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]") #Поле вода "Комментарий для курьера" в форме заказа
    BUTTON_FORM_RENT_ORDER = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")  # Кнопка "Заказать" в форме "Заказать"
    #Модальное окно "Хотите оформить заказ?"
    BUTTON_ORDER_YES = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Да']")  # Кнопка "Да" в модальном окне "Хотите оформить заказ?"
    #Модальное окно "Заказ оформлен"
    BUTTON_ORDER_VIEW_STATUS = (By.XPATH, "//div[contains(@class,'Order_NextButton')]/button[text()='Посмотреть статус']")  # Кнопка "Посмотреть статус" в модальном окне "Заказ оформлен?"