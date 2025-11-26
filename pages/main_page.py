import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from pages.base_page import BasePage
from config import Config
from locators import MainPageLocators, OrderFeedPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.MAIN_URL
        self.locators = MainPageLocators()


    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_button_profile_page(self):
        self.click_on_element(self.locators.BUTTON_PROFILE_ACCOUNT)


    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_button(self):
        self.wait_invisibility_of_element(OrderFeedPageLocators.MODAL_OVERLAY)
        self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)


    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_on_feed_order_button(self):
        self.click_on_element(self.locators.FEED_BUTTON)


    @allure.step("Клик по ингредиенту в конструкторе")
    def click_on_ingredient_in_constructor(self):
        self.wait_invisibility_of_element(OrderFeedPageLocators.MODAL_OVERLAY)
        self.click_on_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)


    @allure.step("Закрытие модального окна ингредиента")
    def click_on_close_modal(self):
        self.wait_modal_opened(OrderFeedPageLocators.MODAL_OPENED)
        self.click_on_element(self.locators.CLOSE_BUN_TITLE_IN_MODAL)


    @allure.step("Клик по кнопке 'Оформить заказ' и ждем анимацию оформления")
    def click_on_button_order(self):
        self.click_on_element(self.locators.BUTTON_ORDER)
        self.wait_invisibility_of_element(OrderFeedPageLocators.ORDER_MODAL_WINDOW_WITHOUT_LOADER)
        self.wait_visibility_of_element(self.locators.SUCCESS_ORDER_INDICATOR)


    @allure.step("Проверка заголовка формы конструктора")
    def check_text_on_constructor_title(self):
        self.wait_visibility_of_element(self.locators.CONSTRUCTOR_TITLE)
        tex_title_form_constructor =  self.get_text_element(self.locators.CONSTRUCTOR_TITLE)
        return tex_title_form_constructor == Data.text_title_on_constructor_form


    @allure.step("Проверка уведомления о принятии заказа")
    def check_text_order_acceptance_notification(self):
        self.wait_modal_opened(OrderFeedPageLocators.MODAL_OPENED)
        notification_text =  self.get_text_element(self.locators.ORDER_ACCEPTANCE_NOTIFICATION)
        return  notification_text == Data.text_order_acceptance_notification


    @allure.step("Проверка появления изображения ингредиента в модальном окне")
    def is_image_bun_in_module_window_visible(self):
        self.wait_modal_opened(OrderFeedPageLocators.MODAL_OPENED)
        return self.is_element_visible(self.locators.BUN_STATS_IN_MODAL)


    @allure.step("Проверка закрытия модального окна заказа")
    def is_modal_bun_closed(self):
        return self.is_disappeared(OrderFeedPageLocators.MODAL_OPENED)


    @allure.step("Добавление булки в заказ (клик по ингредиенту)")
    def add_bun_to_order(self):
        self.wait_invisibility_of_element(OrderFeedPageLocators.MODAL_OVERLAY)
        self.wait_visibility_of_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)
        self.click_on_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)
        self.wait_for(
            lambda d: (
                    len(d.find_elements(*self.locators.BUN_IN_CONSTRUCTOR_TOP)) > 0 or
                    len(d.find_elements(*self.locators.BUN_IN_CONSTRUCTOR_BOTTOM)) > 0
            ),
            timeout=20,
            message="Булка не появилась в конструкторе после клика"
        )

        allure.attach("Булка успешно добавлена в конструктор", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)


    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        self.click_on_element(self.locators.CLOSE_ORDER_MODAL)
        self.wait_modal_closed(OrderFeedPageLocators.MODAL_OPENED)


    @allure.step("Создание заказа и закрытие модального окна")
    def create_order_and_close_modal(self):
        self.drag_ingredient_to_constructor()
        self.click_on_button_order()
        self.close_order_modal()


    @allure.step("Создание заказа на главной странице и переход в ленту заказов")
    def create_order_on_main_and_return_to_feed(self):
        if self.driver.current_url != self.url:
            self.open()
            self.wait_main_page_loaded()

        self.drag_ingredient_to_constructor()
        self.click_on_button_order()
        self.close_order_modal()
        self.click_on_feed_order_button()


    @allure.step("Получение номера заказа из модального окна")
    def get_number_order_from_modal_window(self):
        def _is_real_number(driver):
            try:
                text = self.get_text_element(self.locators.NUMBER_ORDER_IN_MODAL)
                return text != '9999' and text.strip().isdigit()
            except:
                return False

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException

        try:
            WebDriverWait(self.driver, 15).until(
                lambda d: _is_real_number(d),
                message="Номер заказа так и остался '9999' или не стал числом"
            )
            real_number = self.get_text_element(self.locators.NUMBER_ORDER_IN_MODAL)
            return real_number
        except TimeoutException:
            current = self.get_text_element(self.locators.NUMBER_ORDER_IN_MODAL)
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="order_number_still_9999",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Не удалось получить реальный номер заказа. Текущее значение: '{current}'")


    @allure.step("Получить значение счётчика булки")
    def get_bun_counter(self):
        self.wait_visibility_of_element(self.locators.BUN_COUNTER)
        return self.get_text_element(self.locators.BUN_COUNTER)

    @allure.step("Ожидание загрузки главной страницы")
    def wait_main_page_loaded(self):
        self.wait_visibility_of_element(self.locators.CONSTRUCTOR_TITLE)

    @allure.step("Перетаскивание ингредиента в конструктор")
    def drag_ingredient_to_constructor(self):
        self.wait_visibility_of_element(self.locators.BURGER_CONSTRUCTOR)
        self.wait_visibility_of_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)
        ingredient = self.driver.find_element(*self.locators.INGREDIENT_IN_CONSTRUCTOR)
        constructor_zone = self.driver.find_element(*self.locators.BURGER_CONSTRUCTOR)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor_zone).perform()
        self.wait_for(
            lambda d: self.check_value_counter_buns(),
            timeout=20,
            message="Счётчик булок не обновился после перетаскивания"
        )


    @allure.step("Проверка значения счётчика ингредиента после перетаскивания ингредиента")
    def check_value_counter_buns(self):
        value = self.get_text_element(self.locators.BUN_COUNTER)
        return value == '2'