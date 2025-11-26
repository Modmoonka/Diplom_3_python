import allure
from pages.password_recovery_page import ForgotPasswordPage
from pages.login_page import LoginPage
from config import Config
from data import Data


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    @allure.story("Пользователь может перейти на страницу восстановления с формы логина")
    def test_navigate_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_on_forgot_password()
        forgot_password_page = ForgotPasswordPage(driver)
        current_url = forgot_password_page.get_current_url()
        assert current_url == Config.FORGOT_PASSWORD_URL, f"Ожидалось '{Config.FORGOT_PASSWORD_URL}', но получили '{current_url}'"

    @allure.title("Успешная отправка email для восстановления пароля")
    @allure.story("Пользователь вводит email и переходит на страницу сброса пароля")
    def test_submit_email_for_password_recovery(self, driver):
        with allure.step("Открыть страницу восстановления пароля"):
            forgot_password_page = ForgotPasswordPage(driver)
            forgot_password_page.open()

        with allure.step("Ввести email и нажать кнопку 'Восстановить'"):
            forgot_password_page.fill_form_recovery_email(Data.EMAIL_FOR_RECOVERY)
            forgot_password_page.click_on_button_recovery()
            forgot_password_page.wait_for_url(Config.RESET_PASSWORD_URL)

        with allure.step("Проверить переход на страницу ввода нового пароля"):
            assert forgot_password_page.get_current_url() == Config.RESET_PASSWORD_URL

    @allure.title("Поле пароля подсвечивается при переключении видимости")
    @allure.story("Пользователь может видеть/скрывать пароль и видеть активное состояние поля")
    def test_toggle_password_visibility_and_highlight_input(self, driver):
        with allure.step("Открыть страницу восстановления и пройти до формы ввода нового пароля"):
            forgot_password_page = ForgotPasswordPage(driver)
            forgot_password_page.open()
            forgot_password_page.fill_form_recovery_email(Data.EMAIL_FOR_RECOVERY)
            forgot_password_page.click_on_button_recovery()
            forgot_password_page.wait_for_url(Config.RESET_PASSWORD_URL)

        with allure.step("Ввести пароль и нажать иконку показа/скрытия"):
            forgot_password_page.fill_form_recovery_password(Data.PASSWORD_FOR_RECOVERY)
            forgot_password_page.click_icon_show_password()

        with allure.step("Проверить, что поле пароля находится в активном состоянии (подсвечено)"):
            assert  forgot_password_page.is_password_input_active(),"Поле пароля не подсвечено после клика по иконке видимости"