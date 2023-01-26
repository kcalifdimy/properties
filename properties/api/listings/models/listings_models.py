import uuid
from django.conf import settings
from django.db import models
# Create your models here.
from django.utils.timezone import now
#from properties.api.listings.models import Image
#from properties.api.listings.models import Tags





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

    lister = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True )
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField(blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    property_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSES)
    sqft = models.IntegerField(blank=True, null=True)
    open_house = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)
    #images= models.ManyToManyField(Image, related_name='listings', blank=True, )
    #tag = models.ManyToManyField(Tags, related_name='list_tags', blank=True, null=True)

    def __str__(self):
        return self.title


