from django.urls import path

from rest_framework import routers
from .views import EmployeeViewSet, ReviewViewSet

router = routers.DefaultRouter()

router.register('employees', EmployeeViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls