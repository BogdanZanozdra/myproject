from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Get users greater some age'

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='Users age')

    def handle(self, *args, **kwargs):
        age = kwargs['age']
        users = User.objects.filter(age__gt=age)
        self.stdout.write(f'{users}')
