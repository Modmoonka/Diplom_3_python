import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from config import Config
from locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.LOGIN_URL
        self.locators = LoginPageLocators()


    @allure.step("Открытие страницы логина")
    def open(self):
        super().open()


    @allure.step("Ввод email")
    def enter_email(self, email):
        self.fill_input(self.locators.EMAIL_INPUT, email)


    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.fill_input(self.locators.PASSWORD_INPUT, password)


    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_on_forgot_password(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, "div.Modal_modal_overlay__")) == 0
            )
        except TimeoutException:
            pass
        self.click_on_element(self.locators.FORGOT_PASSWORD_BUTTON)


    @allure.step("Авторизация")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_element(self.locators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT)


    @allure.step("Проверка видимости кнопки входа")
    def is_login_button_visible(self):
        return self.is_element_visible(self.locators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT)


    @allure.step("Проверка, что открыта страница логина")
    def is_on_login_page(self):
        return self.get_current_url() == self.url