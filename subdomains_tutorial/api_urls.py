from django.urls import path, include

urlpatterns = [
    path('', include('polls.api.urls')),
]
