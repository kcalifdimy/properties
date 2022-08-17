from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
                                        ListAPIView, RetrieveAPIView, 
                                        CreateAPIView, ListCreateAPIView
                                    )
from rest_framework import permissions
from rest_framework import status

from .models import Listing
from .serializers import ListingSerializer, listingDetailSerializer
from datetime import datetime, timezone, timedelta




class ListingListView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = 'slug'

