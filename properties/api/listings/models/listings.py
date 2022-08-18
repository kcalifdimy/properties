import uuid
from django.db import models
# Create your models here.

from django.utils.timezone import now
from django.conf import settings


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
    
    class HomeType(models.TextChoices):
        HOUSES = 'Houses'
        OFFICE_SPACES = 'Office Spaces'
        LANDS = 'Lands'
        SEMI_DETACHED_BUNGALOW = 'Semi Detached Bungalow'
        DETACHED_BUNGALOW = 'Detached Bungalow'
        SEMI_DETACHED_DUPLEX = 'Semi Detached Duplex'
        DETACHED_DUPLEX = 'Detached Duplex'
        CO_WORKING_SPACE = 'Co-working Space'
        WAREHOUSE = 'Warehouse'
        SHOP_IN_A_MALL = 'Shop in a mall'
        SELF_CONTAIN = 'Self Contain'
        MINI_FLATS = 'Mini Flat'
        TERRACED_BUNGALOW = 'terraced bungalow'
        TERRACED_DUPLEX = 'terraced duplex'
        COMMERCIAL_PROPERTIES = 'Commercial Properties'

    lister = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings', null=True, blank=True )
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    #zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    property_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSES)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    #photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title

