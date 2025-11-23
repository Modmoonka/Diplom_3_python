import allure

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = None


    @allure.step('Открытие страницы')
    def open(self):
        self.driver.get(self.url)
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.Modal_modal_overlay__"))
            )
        except TimeoutException:
            pass


    @allure.step('Ожидание импута и ввод значения')
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)


    @allure.step('Ожидание видимости элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))


    @allure.step('Ожидание исчезновения элемента')
    def wait_invisibility_of_element(self, locator, timeout=Config.DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    @allure.step('Получение текста элемента')
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text


    @allure.step('Получение текста из всех элементов')
    def get_texts_from_elements(self, locator):
        self.wait_visibility_of_element(locator)
        elements = self.driver.find_elements(*locator)
        number_order = []
        for item in elements:
            number_order.append(item.text.strip())
        return number_order


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
    def is_element_disappeared(self, locator, timeout=3):
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
        return self.is_element_disappeared(locator)


    @allure.step('Ожидание появления модального окна')
    def wait_modal_opened(self, locator):
        self.wait_visibility_of_element(locator)


    @allure.step('Ожидание закрытия модального окна')
    def wait_modal_closed(self, locator):
        self.is_disappeared(locator)


    @allure.step('Прокрутка элемента и клик по нему')
    def scroll_to_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.element_to_be_clickable(locator))
        element.click()