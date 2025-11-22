from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка входа в личный кабинет
    BUTTON_ACCOUNT = (By.XPATH, ".//a[@href='/account']")
    # Кнопка перехода на раздел с конструктором
    CONSTRUCTOR_BUTTON = (By.XPATH, './/a[@href="/"]/p')
    FEED_BUTTON = (By.XPATH, './/a[@href="/feed"]/p')
    # Заголовок формы конструктора "соберите бургер"
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
    # Локатор для булочки в конструкторе
    INGREDIENT_IN_CONSTRUCTOR = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')
    # Каунтер
    BUN_COUNTER = (By.XPATH, "//p[contains(text(), 'Краторная булка N-200i')]/preceding-sibling::div[contains(@class, 'counter_')]/p")
    # Подпись с составом (белки, жиры...) в попапе булочки
    BUN_STATS_IN_MODAL = (By.XPATH, "//ul[contains(@class, 'Modal_modal__statsList')]")
    # Закрытие модального окна булки с деталями ингредиента
    CLOSE_BUN_TITLE_IN_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    # Закрытие модального окна булки с деталями ингредиента
    CLOSE_ORDER_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
    # Закрытие модального окна булки с деталями ингредиента
    BURGER_CONSTRUCTOR = (By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7')
    # Кнопка оформить заказ
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    # Уведомление о взятии заказа в модальном окне
    ORDER_ACCEPTANCE_NOTIFICATION = (By.XPATH, "//p[contains(@class, 'undefined text') and text()='Ваш заказ начали готовить' ] ")
    # Номер заказа в модальном окне
    NUMBER_ORDER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large mb-8')]")
    # Иконка с анимацией успешного заказа
    SUCCESS_ORDER_INDICATOR = (By.CSS_SELECTOR, '[alt="tick animation"]')
    # Иконка с анимацией процесса заказа
    LOADING_ORDER_INDICATOR = (By.CSS_SELECTOR, '[alt="loading animation"]')
    # Модальное окно попапа на главной (общее для всех попапов)
    MODAL_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    # Локатор для Оверлея
    MODAL_OVERLAY_WHEN_ORDER_PROCESS = (By.XPATH, '//img[@alt="loading animation"]/following-sibling::div[contains(@class, "Modal_modal_overlay_")]')


class LoginPageLocators:
        # Кнопка восстановить пароль
        FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
        # Кнопка входа в аккаунт на странице login
        SUBMIT_BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти']")


class ForgotPasswordPageLocators:
    # Локатор для заголовка формы восстановления пароля
    FORM_FORGOT_PASSWORD = (By.XPATH ,".//h2[text()='Восстановление пароля']")
    # Локатор для поля ввода email на странице восстановления пароля
    INPUT_EMAIL_FORGOT = (By.XPATH, ".//input[@type='text']")
    # Локатор для кнопки восстановления пароля на странице восстановления
    SUBMIT_BUTTON_ACCOUNT_RECOVERY = (By.XPATH, ".//button[text() = 'Восстановить']")
    # Кнопка войти в форме восстановления пароля
    SUBMIT_BUTTON_FORGOT_FORM = (By.XPATH, ".//p[text() = 'Вспомнили пароль?']/a")
    # Кнопка скрытия/отображения пароля
    HIDE_AND_SHOW_INPUT_PASSWORD = (By.CSS_SELECTOR, ".input__icon svg")
    # Поле ввода пароля на странице восстановления со скрытым паролем
    INPUT_PASSWORD_FORGOT = (By.XPATH, ".//input[@type='password']")
    # Поле ввода пароля в состоянии активно
    INPUT_PASSWORD_IS_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")


class OrderFeedPageLocators:
    # Заголовок формы ленты заказов "Лента заказов"
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    # Первая карточка в ленте заказов
    FIRST_ORDER_CARD_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    # Модальное окно на странице заказов
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    # Локатор для текста состава в модальном окне
    ORDER_TEXT_IN_ORDER_MODAL = (By.XPATH, "//p[text()= 'Cостав']")
    # Итого заказов
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # Итого заказов выполненных сегодня
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Все заказы
    ALL_ORDERS_IN_FEED = (By.XPATH, "//p[starts-with(text(),'#')]")
    # Заказы в работе
    ALL_ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'digits')]")


class ProfilePageLocators:
    # Текст на странице профиля
    ACCOUNT_TEXT_IN_PROFILE = (By.XPATH, ".//p[contains(@class, 'Account_text')]")
    # Кнопка истории заказов
    HISTORY_ORDER_BUTTON_IN_PROFILE = (By.CSS_SELECTOR, 'a[href="/account/order-history"]')
    # Кнопка выхода из профиля
    BUTTON_LOGOUT_PROFILE = (By.XPATH, ".//button[text() = 'Выход']")
    # Все заказы в ленте заказов
    ALL_ORDERS_IN_HISTORY_USER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]//p[contains(@class, 'digits') and not(contains(@class, 'mr-2'))]")
    # Блок основного меню в профиле
    PROFILE_MENU =  (By.XPATH, "//ul[contains(@class, 'Account_list')]")