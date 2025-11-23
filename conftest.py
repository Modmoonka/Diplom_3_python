import pytest
import requests
from selenium.common import TimeoutException

from config import Config

from helpers import generate_random_email, generate_random_string
from driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    web_driver = DriverFactory.get_driver(request.param)
    web_driver.set_window_position(0, 0)
    web_driver.set_window_size(1280, 800)
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def create_user_and_delete():
    email = generate_random_email(5)
    password = generate_random_string(7)
    name = generate_random_string(7)

    payload = {"email": email, "password": password, "name": name}
    response = requests.post(Config.REGISTER_URL, json=payload)
    response_json = response.json()
    token = response_json.get('accessToken')

    yield email, password, token

    if token:
        headers = {'Authorization': f'Bearer {token}'}
        requests.delete(Config.USER_DELETE, headers=headers)


@pytest.fixture()
def login_user_via_localstorage(create_user_and_delete, driver):
    email, password, access_token = create_user_and_delete
    driver.get(Config.LOGIN_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Войти']"))
    )

    driver.execute_script(
        "window.localStorage.setItem('accessToken', arguments[0]);",
        access_token
    )
    driver.get(Config.MAIN_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, './/a[@href="/feed"]/p'))
    )

    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[class^='Modal_modal_overlay__']"))
        )
    except TimeoutException:
        pass

    return email, password