from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     RetrieveAPIView,
                                    )
from rest_framework import permissions
from rest_framework import status
from datetime import datetime, timezone, timedelta
from properties.api.listings.models import Listing
from .serializers import ListingSerializer
from .permissions import IsOwnerOrReadOnly




class ListingListView(ListCreateAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = 'slug'



class ListingRetrieveView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class ListingDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'slug'

    #def get_object(self):
     #   return Listing.objects.get(id=self.kwargs.get("uuid"))
