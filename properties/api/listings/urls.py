from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from properties.api.listings.views import (ListingListView,
                                           ListingDetailView
                                          )


app_name = "listings"


urlpatterns = [
    path('listing/', ListingListView.as_view(), name='listing-list'),
    path('details/<slug>/',  ListingDetailView.as_view(), name='listing-user'),
    
]

