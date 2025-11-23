import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from config import Config
from locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.FORGOT_PASSWORD_URL
        self.locators = ForgotPasswordPageLocators()


    @allure.step("Ввод email для восстановления пароля")
    def fill_form_recovery_email(self, email):
        self.fill_input(self.locators.INPUT_EMAIL_FORGOT, email)


    @allure.step("Клик по кнопке 'Восстановить'")
    def click_on_button_recovery(self):
        self.click_on_element(self.locators.SUBMIT_BUTTON_ACCOUNT_RECOVERY)


    @allure.step("Ввод нового пароля на странице восстановления /reset-password")
    def fill_form_recovery_password(self, password):
        self.fill_input(self.locators.INPUT_PASSWORD_FORGOT, password)


    @allure.step("Клик по иконке показать/скрыть пароль")
    def click_icon_show_password(self):
        self.click_on_element(self.locators.HIDE_AND_SHOW_INPUT_PASSWORD)


    @allure.step("Подсветка поля ввода пароля ")
    def is_password_input_active(self):
        return self.is_element_visible(self.locators.INPUT_PASSWORD_IS_ACTIVE)