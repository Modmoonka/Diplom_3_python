import allure
from locators import ProfilePageLocators
from pages.base_page import BasePage
from config import Config


class  ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.PROFILE_URL
        self.locators = ProfilePageLocators()

    @allure.step("Открытие страницы профиля")
    def open(self):
        super().open()

    @allure.step("Проверка текста на странице профиля")
    def is_profile_info_text_correct(self, expected_text):
        self.wait_visibility_of_element(self.locators.ACCOUNT_TEXT_IN_PROFILE)
        actual_text = self.get_text_element(self.locators.ACCOUNT_TEXT_IN_PROFILE).strip()

        allure.attach(
            f"Ожидалось: '{expected_text}'\nФактически: '{actual_text}'",
            name="Сравнение текста профиля",
            attachment_type=allure.attachment_type.TEXT
        )

        return actual_text == expected_text

    @allure.step("Клик по кнопке 'История заказов'")
    def click_on_history_order_button(self):
        self.wait_visibility_of_element(self.locators.HISTORY_ORDER_BUTTON_IN_PROFILE)
        self.scroll_to_and_click(self.locators.HISTORY_ORDER_BUTTON_IN_PROFILE)

    @allure.step("Клик по кнопке 'Выход' из аккаунта")
    def click_on_logout_button(self):
        self.click_on_element(self.locators.BUTTON_LOGOUT_PROFILE)

    @allure.step("Получение номера последнего заказа в истории")
    def get_last_order_number_in_history_user(self):
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_HISTORY_USER)
        numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_HISTORY_USER)
        number_last_order = numbers[0].lstrip('#0')
        return number_last_order

    @allure.step("Ожидание загрузки страницы профиля")
    def wait_profile_page_loaded(self):
        self.wait_visibility_of_element(self.locators.ACCOUNT_TEXT_IN_PROFILE)