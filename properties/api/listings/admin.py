from django.contrib import admin
from django.contrib import admin
from properties.api.listings.models import Listing, Image
from django.utils.translation import gettext_lazy as _


class ListingAdmin(admin.ModelAdmin):

    list_display = (
                    'lister', 'slug', 'title', 'address','town', 'city', 'state', 'description', 'sale_type', 'price','bedrooms', 'bathrooms',
                    'property_type', 'sqft', 'open_house', 'is_published', 'list_date', 'get_images'
                    )
    list_editable = (
                    'slug', 'title', 'address','town', 'city', 'state', 'description', 'sale_type', 'price','bedrooms', 'bathrooms', 
                    'property_type', 'sqft', 'open_house', 'is_published', 'list_date'
                    )

    def get_queryset(self, request):
        queryset = super(ListingAdmin, self).get_queryset(request)
        queryset = queryset.order_by('lister')
        return queryset
    
    def get_images(self, obj):
        return ",".join([m.images for m in obj.images.all()]) 

admin.site.register(Listing, ListingAdmin)



admin.site.register(Image)

