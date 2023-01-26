from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from django.forms import ImageField as DjangoImageField

from django.db import models
from properties.api.listings.models import Image, Listing
#from properties.api.listings.models import Images
from properties.api.users.models import User
from properties.api.listings.base_serializers import Base64ImageField
from properties.api.users.serializers import UserSerializer


   

class ImageSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)

    class Meta:
        model = Image
        fields = ['id','listing', 'images']
        extra_kwargs = {'listing': {'read_only': True},}  




    
class ListingSerializers(serializers.ModelSerializer):
    #lister = UserSerializer(read_only=True, many=True)
    images = ImageSerializer(many=True, read_only=True)
    #uploaded_images = serializers.ListField(
     #   child=Base64ImageField(allow_empty_file=True, allow_null=True, required=False,max_length=None, use_url=False), 
      #  allow_empty=True, allow_null=True, default = [])
    uploaded_images = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = True, use_url = False),
        write_only = True
        )
    

    def create(self, validated_data):
        # create product
        image_data = validated_data.pop('uploaded_images')
        listing = Listing.objects.create(**validated_data)
        #user = self.context['request'].user
        for image_data in image_data:
            new_list_image =  Image.objects.create(listing=listing, images=image_data)
        return  listing


    def clear_existing_images(self, instance):
        for listing_image in instance.images.all():
            listing_image.images.delete()
            listing_image.delete()
    


    def update(self, instance, validated_data):
        image_data = validated_data.pop('uploaded_images')
        instance = super().update(instance, validated_data)
        instance.save()
        if image_data:
            self.clear_existing_images(instance) # uncomment this if you want to clear existing images.
            listing_image_model_instance = [Image(listing=instance, images=image) for image in image_data]
            Image.objects.bulk_create(
                listing_image_model_instance
            )
        return instance

       


    class Meta:
        model = Listing
        lookup_field = 'slug'
        fields = [
                    'id',
                    'slug',
                    'title',
                    'address',
                    'town',
                    'city',
                    'state', 
                    'price', 
                    'description',
                    'sale_type', 
                    'property_type', 
                    'bedrooms', 
                    'bathrooms', 
                    'sqft', 
                    #'lister',
                    'images',
                    'uploaded_images'
                ]


