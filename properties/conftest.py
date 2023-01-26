import pytest
from rest_framework.test import APIClient


from properties.api.users.models import User, Profile
from properties.api.users.tests.factories import UserFactory, ProfileFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()



@pytest.fixture
def profile() -> Profile:
    return ProfileFactory()



@pytest.fixture()
def client():
    yield APIClient()

