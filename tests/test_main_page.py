import allure
from pages.main_page import MainPage

@allure.epic("Конструктор бургеров")
@allure.feature("Основная страница")
class TestMainPage:

    @allure.title("Переход в раздел 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_main_page_loaded()
        main_page.click_on_constructor_button()
        assert main_page.check_text_on_constructor_title(), 'Не появился заголовок страницы конструктор - соберите бургер'

    @allure.title("Открытие модального окна ингредиента")
    def test_open_modal_window_bun(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_main_page_loaded()
        main_page.click_on_ingredient_in_constructor()
        assert main_page.is_image_bun_in_module_window_visible(), 'Не появился состав ингредиента в модальном окне'

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_main_page_loaded()
        main_page.click_on_ingredient_in_constructor()
        main_page.click_on_close_modal()
        assert main_page.is_modal_bun_closed(), "Модальное окно с булочкой не закрылось"

    @allure.title("Добавление ингредиента в заказ")
    def test_add_ingredient_in_order_drag_and_drop(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        assert main_page.check_value_counter_buns(), "Каунтер ингредиента не изменился"

    @allure.title("Оформление заказа залогиненным пользователем")
    def test_placing_order_logged_user(self, login_user_via_localstorage, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_main_page_loaded()
        main_page.drag_ingredient_to_constructor()
        main_page.click_on_button_order()
        assert main_page.check_text_order_acceptance_notification(), 'Окно с подтверждением заказа не появилось'