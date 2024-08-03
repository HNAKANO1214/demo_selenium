import pytest

from shared.commands.load_seed import load_seed_data


@pytest.fixture(scope='session', autouse=True)
def test_load_seed_data(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        load_seed_data()
