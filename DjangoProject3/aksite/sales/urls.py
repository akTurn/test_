from django.urls import path, include
from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import OfficeViewSet

router = DefaultRouter()
#router = SimpleRouter()
router.register(r'offices', OfficeViewSet,basename='offices')
print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]

