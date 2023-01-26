import uuid


from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from datetime import datetime


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', null=True, blank=True )
    bio = models.TextField(max_length=550, blank=True, default='')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    #description = models.TextField(blank=True)
    address =  models.CharField(_("Addresss of User"), blank=True, max_length=255)



    def __str__(self):
        return f'{self.user}'



      