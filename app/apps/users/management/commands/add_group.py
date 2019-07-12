from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.utils import timezone

class Command(BaseCommand):
    help = 'Add group to urbvan app test'

    def add_arguments(self, parser):
         parser.add_argument('group', type=str, help='Indicates the group name')

    def handle(self, *args, **options):
        group = options['group']

        group = Group.objects.get_or_create(name=group)[0]
        self.stdout.write(self.style.SUCCESS('Successfully created group "%s"' % group.name))
