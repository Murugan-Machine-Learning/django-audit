from django.urls import include, path

from rest_framework import routers

from api.views import UdyamViewSet

router = routers.DefaultRouter()
router.register(r'udyam', UdyamViewSet)

urlpatterns = [
   path('', include(router.urls)),
]