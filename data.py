from faker import Faker
import random
import string

fake = Faker()

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

class Data:
    EMAIL_FOR_RECOVERY = fake.email()
    PASSWORD_FOR_RECOVERY = generate_password()

    USER_CREDENTIALS = {
        "email": fake.email(),
        "password": generate_password(),
        "name": fake.first_name()
    }

    info_text_in_profile_page = 'В этом разделе вы можете изменить свои персональные данные'
    text_title_on_constructor_form = 'Соберите бургер'
    text_title_on_feed_form = 'Лента заказов'
    text_order_acceptance_notification = 'Ваш заказ начали готовить'
    text_module_feed = 'Cостав'