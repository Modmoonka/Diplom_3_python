import pytest
import requests
from config import Config
from data import Data
from driver_factory import DriverFactory


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    web_driver = DriverFactory.get_driver(request.param)
    web_driver.set_window_position(0, 0)
    web_driver.set_window_size(1280, 800)
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def register_new_user_and_return_credentials():
    payload = Data.USER_CREDENTIALS
    email = payload.get('email')
    password = payload.get('password')
    response = requests.post(Config.REGISTER_URL, json=payload)
    if response.status_code == 200:
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        yield email, password, access_token, refresh_token
        headers = {"Authorization": access_token}
        requests.delete(Config.USER_DATA_MANAGMENT_URL, headers=headers)
    else:
        pytest.fail(f"Не удалось зарегистрировать пользователя: {response.status_code}, {response.text}")


@pytest.fixture()
def login_user_via_localstorage(register_new_user_and_return_credentials, driver):
    email, password, access_token, refresh_token = register_new_user_and_return_credentials
    driver.get(Config.BASE_URL)
    script_set_tokens = (
        "window.localStorage.setItem('accessToken', '{}');"
        "window.localStorage.setItem('refreshToken', '{}');"
    ).format(access_token, refresh_token)
    driver.execute_script(script_set_tokens)
    driver.refresh()
    return email, password