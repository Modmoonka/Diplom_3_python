import pytest
import requests
from config import Config
from driver_factory import DriverFactory
from helpers import generate_random_email, generate_random_string  # ← убедитесь, что эти функции доступны


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    web_driver = DriverFactory.get_driver(request.param)
    web_driver.set_window_position(0, 0)
    web_driver.set_window_size(1280, 800)
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def register_new_user_and_return_credentials():
    email = generate_random_email(8)
    password = generate_random_string(8)
    name = generate_random_string(6)

    payload = {"email": email, "password": password, "name": name}
    response = requests.post(Config.REGISTER_URL, json=payload)

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get("accessToken")
        refresh_token = tokens.get("refreshToken")

        yield email, password, access_token, refresh_token

        headers = {"Authorization": f"Bearer {access_token}"}
        requests.delete(Config.USER_DATA_MANAGMENT_URL, headers=headers)
    else:
        pytest.fail(f"Не удалось зарегистрировать пользователя: {response.status_code}, {response.text}")


@pytest.fixture()
def login_user_via_localstorage(register_new_user_and_return_credentials, driver):
    email, password, access_token, refresh_token = register_new_user_and_return_credentials

    # Устанавливаем токены в localStorage
    driver.get(Config.BASE_URL)
    script = (
        f"window.localStorage.setItem('accessToken', '{access_token}');"
        f"window.localStorage.setItem('refreshToken', '{refresh_token}');"
    )
    driver.execute_script(script)
    driver.refresh()

    return email, password