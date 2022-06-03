from rest_framework.routers import DefaultRouter
from .views import TodoViewSet



router = DefaultRouter()
router.register('',TodoViewSet, basename="todoviewset")
urlpatterns  = router.urls