import smtplib
from email.header import Header
from email.mime.text import MIMEText
from decouple import config

def send_email(blog):
    login = config('EMAIL_USER')
    password = config('EMAIL_PASSWORD')
    print(login)
    print(password)

    msg = MIMEText(
        f"Поздравляю, ваша статья {blog.title} "
        f"набрала {blog.views_count} просмотров",
        "plain", "utf-8"
    )
    msg["Subject"] = Header("Поздравляю !!!", "utf-8")
    msg["From"] = login + "@yandex.ru"
    msg["To"] = ",".join(config("EMAIL_TO").split(","))

    s = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10)

    s.starttls()
    s.login(login, password)
    s.sendmail(msg["From"], msg["To"], msg.as_string())

    s.quit()