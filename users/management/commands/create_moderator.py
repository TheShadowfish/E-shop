from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Права доступа ему все равно задаю через админку,
    просто создание пользователя другим методом требует подтверждения почтового ящика,
    а почту делать на яндексе не хочу
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email="moderator@sky.pro",
            first_name="Moderator",
            last_name="SkyPro",
            is_staff=False,
            is_superuser=False,
        )

        user.set_password("1100")
        user.save()
