from rest_framework import serializers
from properties.api.listings.models import Listing
from properties.api.users.models import User




class ListingSeralizer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='listing-detail',
        lookup_field='slug',
    )

    lister = serializers.HyperlinkedRelatedField(
        lookup_field='id',
        view_name='user-detail',
        read_only=True,
        #queryset=User.objects.all()
    
    )

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
                    'url',
                 )
