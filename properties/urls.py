from django.urls import include, path

urlpatterns = [
    path('accounts/', include('properties.api.users.urls', namespace="users")),
    path('listings/', include('properties.api.listings.urls', namespace="listings")),
    path('contacts/', include('properties.api.contacts.urls', namespace="contacts")),





    
    #path("users/", include("caliproperties.users.urls", namespace="users")),

    #path('managers/', include('properties.api.realtors.urls')),

    #path('', include('properties.api.links.urls')),

    
    # Your stuff: custom urls includes go here
] 