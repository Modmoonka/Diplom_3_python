import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import ProfilePage


class TestLoginPage:

    @allure.title("Пользователь может выйти из аккаунта и оказаться на странице логина")
    @allure.story("Разлогиниться через профиль")
    def test_logout_user(self, driver, login_user_via_localstorage):
        with allure.step("Перейти в личный кабинет"):
            main_page = MainPage(driver)
            main_page.click_on_button_profile_page()

        with allure.step("Выполнить выход из аккаунта"):
            profile_page = ProfilePage(driver)
            profile_page.click_on_logout_button()

        with allure.step("Очистить сессию (cookies + localStorage)"):
            from pages.base_page import BasePage
            base = BasePage(driver)
            base.clear_browser_data()

        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Убедиться, что отображается форма логина"):
            assert login_page.is_login_page_loaded(), "Форма логина не загружена"