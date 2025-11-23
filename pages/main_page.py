import allure

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from pages.base_page import BasePage
from config import Config
from locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.MAIN_URL
        self.locators = MainPageLocators()


    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_button_profile_page(self):
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[class^='Modal_modal_overlay__']"))
        )
        element = self.driver.find_element(*self.locators.BUTTON_PROFILE_ACCOUNT)

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)


    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_button(self):
        self.wait_invisibility_of_element(self.locators.MODAL_OVERLAY_WHEN_ORDER_PROCESS)
        self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)


    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_on_feed_order_button(self):
        self.click_on_element(self.locators.FEED_BUTTON)


    @allure.step("Клик по ингредиенту в конструкторе")
    def click_on_ingredient_in_constructor(self):
        self.wait_invisibility_of_element(self.locators.MODAL_OVERLAY_WHEN_ORDER_PROCESS)
        self.click_on_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)


    @allure.step("Закрытие модального окна ингредиента")
    def click_on_close_modal(self):
        self.wait_modal_opened(self.locators.MODAL_OPENED)
        self.click_on_element(self.locators.CLOSE_BUN_TITLE_IN_MODAL)


    @allure.step("Клик по кнопке 'Оформить заказ' и ждем анимацию оформления")
    def click_on_button_order(self):
        self.click_on_element(self.locators.BUTTON_ORDER)
        self.wait_visibility_of_element(self.locators.LOADING_ORDER_INDICATOR)
        self.wait_invisibility_of_element(self.locators.MODAL_OVERLAY_WHEN_ORDER_PROCESS)
        self.wait_visibility_of_element(self.locators.SUCCESS_ORDER_INDICATOR)


    @allure.step("Проверка заголовка формы конструктора")
    def check_text_on_constructor_title(self):
        self.wait_visibility_of_element(self.locators.CONSTRUCTOR_TITLE)
        tex_title_form_constructor =  self.get_text_element(self.locators.CONSTRUCTOR_TITLE)
        return tex_title_form_constructor == Data.text_title_on_constructor_form


    @allure.step("Проверка уведомления о принятии заказа")
    def check_text_order_acceptance_notification(self):
        self.wait_modal_opened(self.locators.MODAL_OPENED)
        notification_text =  self.get_text_element(self.locators.ORDER_ACCEPTANCE_NOTIFICATION)
        return  notification_text == Data.text_order_acceptance_notification


    @allure.step("Проверка появления изображения ингредиента в модальном окне")
    def is_image_bun_in_module_window_visible(self):
        self.wait_modal_opened(self.locators.MODAL_OPENED)
        return self.is_element_visible(self.locators.BUN_STATS_IN_MODAL)


    @allure.step("Проверка закрытия модального окна заказа")
    def is_modal_bun_closed(self):
        return self.is_modal_closed(self.locators.MODAL_OPENED)


    @allure.step("Добавление булки в заказ (клик по ингредиенту)")
    def add_bun_to_order(self):
        self.wait_invisibility_of_element(self.locators.MODAL_OVERLAY_WHEN_ORDER_PROCESS)
        self.wait_visibility_of_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)
        self.click_on_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)

        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            lambda d: self.get_text_element(self.locators.BUN_COUNTER) == "2")


    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        self.click_on_element(self.locators.CLOSE_ORDER_MODAL)
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "div.Modal_modal_overlay__")) == 0
        )


    @allure.step("Создание заказа и закрытие модального окна")
    def create_order_and_close_modal(self):
        self.add_bun_to_order()
        self.click_on_button_order()
        self.close_order_modal()


    @allure.step("Создание заказа на главной странице и переход в ленту заказов")
    def create_order_on_main_and_return_to_feed(self):
        self.click_on_constructor_button()
        self.create_order_and_close_modal()
        self.click_on_feed_order_button()


    @allure.step("Получение номера заказа из модального окна")
    def get_number_order_from_modal_window(self):
        return self.get_text_element(self.locators.NUMBER_ORDER_IN_MODAL)

    @allure.step("Получить значение счётчика булки")
    def get_bun_counter(self):
        self.wait_visibility_of_element(self.locators.BUN_COUNTER)
        return self.get_text_element(self.locators.BUN_COUNTER)