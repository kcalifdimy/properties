from django.urls import path
from properties.api.contacts.views import ContactCreateView





app_name = "contacts"

urlpatterns = [
    path('contact/', ContactCreateView.as_view()),
]
