from django.urls import path

urlpatterns = [
    path('users', include('users.urls')),
    path('reviews', include('reviews.urls')),
    path('petsitters', include('petsitters.urls')),
]