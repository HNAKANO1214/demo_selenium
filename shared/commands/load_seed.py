
import django
import os
import sys

from dotenv import load_dotenv

from django.core.management import call_command

sys.path.append(os.getcwd())
load_dotenv()
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'config.settings.local')
)
django.setup()

LOAD_SEED_DATA = [
    'shared/fixtures/seeders/constructor_standing.json',
    'shared/fixtures/seeders/driver_standing.json',
    'shared/fixtures/seeders/race_reslut.json',
]


def load_seed_data():
    print('Loading seed data...')
    for seed_data in LOAD_SEED_DATA:
        print(f'Loading {seed_data}...')
        call_command('loaddata', seed_data)
        print(f'{seed_data} loaded.')
    print('Seed data loaded.')


if __name__ == '__main__':
    load_seed_data()
