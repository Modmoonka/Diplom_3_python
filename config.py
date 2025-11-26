class Config:

    # Страницы
    BASE_URL = "https://stellarburgers.education-services.ru"

    LOGIN_URL = f'{BASE_URL}/login'
    MAIN_URL = f'{BASE_URL}/'
    REGISTER_URL = f'{BASE_URL}/api/auth/register'
    PROFILE_URL = f'{BASE_URL}/account/profile'
    ORDERS_URL = f'{BASE_URL}/account/order-history'
    ACCOUNT_URL = f'{BASE_URL}/account'
    FEED_URL = f'{BASE_URL}/feed'
    FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'
    RESET_PASSWORD_URL = f'{BASE_URL}/reset-password'
    USER_DELETE = f'{BASE_URL}/user'
    USER_DATA_MANAGMENT_URL= f'{BASE_URL}/api/auth/user'

    # Таймауты
    DEFAULT_TIMEOUT = 10