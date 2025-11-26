import allure
from data import Data
from pages.base_page import BasePage
from config import Config
from locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.FEED_URL
        self.locators = OrderFeedPageLocators()

    @allure.step("Проверка появления заголовка формы ленты заказов")
    def check_text_on_feed_title(self):
        self.wait_visibility_of_element(self.locators.FEED_TITLE)
        text_title_form_feed = self.get_text_element(self.locators.FEED_TITLE)
        return  text_title_form_feed == Data.text_title_on_feed_form


    @allure.step("Клик по карточке заказа")
    def click_on_order_card(self):
        self.click_on_element(self.locators.FIRST_ORDER_CARD_IN_FEED)


    @allure.step("Проверка текста в модальном окне заказа")
    def check_text_order_in_modal(self):
        self.wait_modal_opened(OrderFeedPageLocators.MODAL_OPENED)
        order_text =  self.get_text_element(self.locators.ORDER_TEXT_IN_ORDER_MODAL)
        return  order_text == Data.text_module_feed


    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self):
        self.wait_visibility_of_element(self.locators.TOTAL_ORDERS_COUNTER)
        return int(self.get_text_element(self.locators.TOTAL_ORDERS_COUNTER))


    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        self.wait_visibility_of_element(self.locators.TODAY_ORDERS_COUNTER)
        return  int(self.get_text_element(self.locators.TODAY_ORDERS_COUNTER))


    @allure.step("Получение списка номеров заказов в ленте заказов")
    def get_all_order_numbers_feed(self):
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_FEED)
        raw_numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_FEED)
        return [num.lstrip('#') for num in raw_numbers]


    @allure.step("Получение списка номеров заказов в работе")
    def get_all_order_numbers_in_progress(self):
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_FEED)
        raw_numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_FEED)
        cleaned_numbers = []
        for text in raw_numbers:
            if text.startswith("#"):
                text = text[1:]
            cleaned_numbers.append(text.lstrip('0'))
        return cleaned_numbers

    def wait_feed_page_loaded(self):
        self.wait_visibility_of_element(self.locators.FEED_TITLE)