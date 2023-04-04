import pytest
from decouple import config
from django.conf import settings


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': config("TEST_POSTGRES_DB"),
        'USER': config("TEST_POSTGRES_USER"),
        'PASSWORD': config("TEST_POSTGRES_PASSWORD"),
        'HOST': config("TEST_POSTGRES_HOST"),
        'PORT': config("TEST_POSTGRES_PORT"),
        'ATOMIC_REQUESTS': True,
    }
