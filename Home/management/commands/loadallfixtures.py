from django.template.defaultfilters import default

from elearningplatform.settings import BASE_DIR
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load all fixtures automatically from all apps"

    def handle(self, *args, **options):
        fixtures = [BASE_DIR / 'User/fixtures/user_data.json', BASE_DIR / 'User/fixtures/lecturer_data.json']

        fixtures.extend(BASE_DIR.glob('Courses/fixtures/*.json'))
        fixtures.extend(BASE_DIR.glob('Home/fixtures/*.json'))
        fixtures.extend(BASE_DIR.glob('Classwork/fixtures/*.json'))

        fixtures.append(BASE_DIR / 'User/fixtures/student_data.json')

        management.call_command('makemigrations')
        management.call_command('migrate')
        for fixture in fixtures:
            print(fixture)
            management.call_command('loaddata', fixture)
