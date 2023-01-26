from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from properties.api.listings import views


app_name = "listings"

router = SimpleRouter()
router.register(r'listing', views.ListingViewSet)

urlpatterns = [
    path('search', views.SearchView.as_view()),
]

urlpatterns += router.urls