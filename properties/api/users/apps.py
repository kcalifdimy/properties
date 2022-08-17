from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "properties.api.users"
    label = "users"

    def ready(self):
        from . import signals  # noqa