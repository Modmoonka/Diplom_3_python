import allure
from pages.main_page import MainPage
from pages.account_page import ProfilePage
from config import Config


class TestProfilePage:

    @allure.title("Переход в личный кабинет авторизованного пользователя")
    def test_navigate_to_profile(self, driver, login_user_via_localstorage):
        main_page = MainPage(driver)
        main_page.click_on_button_profile_page()
        profile_page = ProfilePage(driver)
        profile_page.wait_profile_page_loaded()
        expected_text = "В этом разделе вы можете изменить свои персональные данные"
        assert profile_page.is_profile_info_text_correct(expected_text), \
            'Не удалось перейти в личный кабинет'

    @allure.title("Переход в раздел 'История заказов' авторизованного пользователя")
    def test_navigate_to_history_order_profile(self, driver, login_user_via_localstorage):
        main_page = MainPage(driver)
        main_page.click_on_button_profile_page()
        profile_page = ProfilePage(driver)
        profile_page.click_on_history_order_button()
        profile_page.wait_for_url(Config.ORDERS_URL)
        assert profile_page.get_current_url() == Config.ORDERS_URL, \
            f"Ожидался URL '{Config.ORDERS_URL}', но получен '{profile_page.get_current_url()}'"