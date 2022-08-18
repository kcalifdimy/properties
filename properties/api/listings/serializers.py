from rest_framework import serializers
from properties.api.listings.models import Listing
from properties.api.users.models import User




class ListingSerializer(serializers.ModelSerializer):
   

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            validated_data['lister'] = user

        listing = Listing(**validated_data)
        listing.save()
        return listing

    class Meta:
        model = Listing
        fields = (
                    'id',
                    'title',
                    'address',
                    'city',
                    'state', 
                    'price', 
                    'sale_type', 
                    'property_type', 
                    'bedrooms', 
                    'bathrooms', 
                    'sqft', 
                    'slug',
                    'lister',
                 )
