from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EventViewSet, LocationViewSet

router = DefaultRouter()
router.register("event", EventViewSet)
router.register("location", LocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
