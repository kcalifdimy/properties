from django.urls import include, path

urlpatterns = [
    path('accounts/', include('properties.api.users.urls', namespace="users")),


    
    #path("users/", include("caliproperties.users.urls", namespace="users")),

    #path('managers/', include('properties.api.realtors.urls')),

    #path('', include('properties.api.links.urls')),

    
    # Your stuff: custom urls includes go here
] 