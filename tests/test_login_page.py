import allure

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from locators import LoginPageLocators
from pages.main_page import MainPage
from pages.account_page import ProfilePage
from config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage:

    @allure.title("Выход из аккаунта")
    def test_logout_user(self, driver, login_user_via_localstorage):

        main_page = MainPage(driver)
        main_page.click_on_button_profile_page()
        profile_page = ProfilePage(driver)
        profile_page.click_on_logout_button()

        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")

        driver.get(Config.LOGIN_URL)

        OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__")
        try:
            WebDriverWait(driver, 5).until_not(
                EC.presence_of_element_located(OVERLAY)
            )
        except TimeoutException:
            pass

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
        )

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT)
        )