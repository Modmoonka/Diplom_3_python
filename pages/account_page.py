import allure

from locators import ProfilePageLocators
from pages.base_page import BasePage
from config import Config


class  ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.PROFILE_URL
        self.locators = ProfilePageLocators()

    def open(self):
        self.driver.get(self.url)

    @allure.step("Открытие страницы профиля")
    def open(self):
        super().open()

    @allure.step("Проверка текста на странице профиля")
    def is_profile_info_text_correct(self, expected_text):
        try:
            self.wait_visibility_of_element(self.locators.ACCOUNT_TEXT_IN_PROFILE)
            actual_text = self.get_text_element(self.locators.ACCOUNT_TEXT_IN_PROFILE).strip()
            return actual_text == expected_text
        except Exception as e:
            print(f"Ошибка при проверке текста профиля: {e}")
            return False

    @allure.step("Клик по кнопке 'История заказов'")
    def click_on_history_order_button(self):
        self.wait_visibility_of_element(self.locators.HISTORY_ORDER_BUTTON_IN_PROFILE)
        self.scroll_to_and_click(self.locators.HISTORY_ORDER_BUTTON_IN_PROFILE)

    @allure.step("Клик по кнопке 'Выход' из аккаунта")
    def click_on_logout_button(self):
        self.click_on_element(self.locators.BUTTON_LOGOUT_PROFILE)

    @allure.step("Получение номера последнего заказа в истории")
    def get_latest_order_number(self):
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_HISTORY_USER)
        order_numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_HISTORY_USER)
        return order_numbers[0] if order_numbers else None