import uuid
from django.db import models
# Create your models here.
from django.utils.timezone import now
from django.conf import settings
from properties.api.listings.models import Listing



class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

