import allure
from selenium import webdriver


# Функция setup_class
@allure.step('Создаем веб драйвер')
def setup_class():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

# Функция teardown_class
@allure.step('Закрываем браузер')
def teardown_class(cls):
    cls.driver.quit()

# Регистрация функций setup_class и teardown_class в PyTest
def pytest_configure(config):
    config.pluginmanager.register(setup_class, "setup_class")
    config.pluginmanager.register(teardown_class, "teardown_class")