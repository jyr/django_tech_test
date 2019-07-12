from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone

class Command(BaseCommand):
    help = 'Add user to urbvan app test'

    def add_arguments(self, parser):
         parser.add_argument('username', type=str, help='Indicates the username')
         parser.add_argument('password', type=str, help='Indicates the password')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        user = User.objects.get_or_create(username=username, email='', password=password)[0]
        self.stdout.write(self.style.SUCCESS('Successfully created user "%s"' % user.username))
