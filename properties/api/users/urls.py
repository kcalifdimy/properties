from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from .views import (
                    SignupView, UserListView, UserRetrieveView, 
                    UpdateUserView, 
                    #ProfileRetrieveView, 
                    #ProfileCreateView,
                    #ProfileUpdateView, 
                    )


app_name = "users"


urlpatterns = [
    path('signup', SignupView.as_view(), name='signup_user'),
    path('list_users', UserListView.as_view(), name='list_users'),
    path('retrieve_user/<uuid:uuid>', UserRetrieveView.as_view(), name='retrieve_user'),
    path('update_user/<uuid:uuid>', UpdateUserView.as_view(), name='update_user'),
    #path('add_profile',  ProfileCreateView.as_view(), name='list_profile'),
    #path('retrieve_profile/<uuid:uuid>',  ProfileRetrieveView.as_view(), name='retrieve_profile'),
    #path('update_profile/<uuid:uuid>',  ProfileUpdateView.as_view(), name='update_profile'),

]

