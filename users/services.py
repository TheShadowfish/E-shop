import secrets
import string

from django.core.mail import send_mail

from config import settings


def send_email_confirmation(url, user_email):
    send_mail(
        subject="Подтверждение почты",
        message=f"Привет, перейди по ссылке для подтверждения почты {url}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
    )

def generate_password():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(12))
        if (
                any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
        ):
            break
    return password


def send_email_password(email, password):


    # print(f"Пароль {password}")

    message = f"Привет, держи новый сложный 12-ти символьный пароль, который ты тоже забудешь: {password}. \
                        Если вы не запрашивали восстановление пароля, просто игнорируйте это сообщение."

    # print(f"Пароль {message}")

    send_mail(
        subject="Восстановление пароля",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
