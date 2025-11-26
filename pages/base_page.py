import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderFeedPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = None


    @allure.step('Открытие страницы')
    def open(self):
        self.driver.get(self.url)
        try:
            WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
                EC.invisibility_of_element_located(OrderFeedPageLocators.MODAL_OVERLAY)
            )
        except TimeoutException:
            pass


    @allure.step('Ожидание импута и ввод значения')
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)


    @allure.step('Ожидание видимости элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))


    @allure.step('Ожидание исчезновения элемента')
    def wait_invisibility_of_element(self, locator, timeout=Config.DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Клик по элементу')
    def click_on_element(self, locator, wait_for_overlay=True):
        if wait_for_overlay:
            try:
                WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
                    EC.invisibility_of_element_located(OrderFeedPageLocators.MODAL_OVERLAY)
                )
            except TimeoutException:
                pass

        element = WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)


    @allure.step('Получение текста элемента')
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text


    @allure.step('Получение текста из всех элементов')
    def get_texts_from_elements(self, locator):
        self.wait_visibility_of_element(locator)
        elements = self.driver.find_elements(*locator)
        return [item.text.strip() for item in elements]


    @allure.step('Ожидание текущего URL, ожидание появления expected_url, если он передан')
    def get_current_url(self, expected_url=None, timeout=Config.DEFAULT_TIMEOUT):
        if expected_url:
            WebDriverWait(self.driver, timeout).until(
                EC.url_to_be(expected_url)
            )
        return self.driver.current_url

    @allure.step('Ожидание, что URL станет ожидаемым')
    def wait_for_url(self, expected_url, timeout=Config.DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))


    @allure.step('Ожидание исчезновения элемента из дерева')
    def is_disappeared(self, locator, timeout=Config.DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False


    @allure.step('Проверка видимости элемента')
    def is_element_visible(self, locator):
        try:
            self.wait_visibility_of_element(locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Проверка закрытия модального окна')
    def is_modal_closed(self, locator):
        try:
            self.is_disappeared(locator)
            return True
        except TimeoutException:
            return False


    @allure.step('Ожидание появления модального окна')
    def wait_modal_opened(self, locator):
        self.wait_visibility_of_element(locator)


    @allure.step('Ожидание закрытия модального окна')
    def wait_modal_closed(self, locator):
        self.is_disappeared(locator)

    @allure.step('Прокрутка элемента и клик по нему')
    def scroll_to_and_click(self, locator, wait_for_overlay=True):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.click_on_element(locator, wait_for_overlay=wait_for_overlay)


    @allure.step("Ожидание выполнения пользовательского условия")
    def wait_for(self, condition_func, timeout=Config.DEFAULT_TIMEOUT, message=""):
        WebDriverWait(self.driver, timeout).until(lambda d: condition_func(d), message=message)

    @allure.step("Очистка cookies и localStorage")
    def clear_browser_data(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear()")

    @allure.step("Ожидание отсутствия элементов по локатору")
    def wait_for_elements_absence(self, locator, timeout=Config.DEFAULT_TIMEOUT):
        self.wait_for(
            lambda d: len(d.find_elements(*locator)) == 0,
            timeout=timeout,
            message=f"Элементы по локатору {locator} всё ещё присутствуют"
        )

    @allure.step("Перетащить элемент на целевую область")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()



