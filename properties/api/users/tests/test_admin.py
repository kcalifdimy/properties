import pytest
from django.urls import reverse

from properties.api.users.models import User

pytestmark = pytest.mark.django_db


class TestUserAdmin:
    
    def test_an_admin_view(self, admin_client):
        response = admin_client.get('/admin/')
        assert response.status_code == 200