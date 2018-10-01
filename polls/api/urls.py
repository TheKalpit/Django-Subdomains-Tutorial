from django.urls import include, path
from rest_framework import routers

from polls.api import views

router = routers.SimpleRouter()
router.register(r'polls', views.PollViewSet, base_name='polls')

urlpatterns = [
    path('', include(router.urls)),
]
