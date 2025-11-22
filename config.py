class Config:

    # Страницы
    BASE_URL = "https://stellarburgers.education-services.ru"

    LOGIN_URL = f'{BASE_URL}/login'
    MAIN_URL= f'{BASE_URL}/'
    REGISTER_URL = f'{BASE_URL}/register'
    PROFILE_URL = f'{BASE_URL}/account/profile'
    ORDERS_URL = f'{BASE_URL}/account/order-history'
    ACCOUNT_URL = f'{BASE_URL}/account'
    FEED_URL = f'{BASE_URL}/feed'
    FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'
    RESET_PASSWORD_URL= f'{BASE_URL}/reset-password'

    # Таймауты
    DEFAULT_TIMEOUT = 10