from django.core.management import BaseCommand

from d_users.models import D_user


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = D_user.objects.create(email="admin@example.com")
        user.set_password('1100')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()