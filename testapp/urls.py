from django.urls import path, include
from .views import EmployeeModelViewsSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', EmployeeModelViewsSet, basename='empviewset')

urlpatterns = [
    path('', include(router.urls)),
]
