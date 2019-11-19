from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('api/v0/students', StudentsViewSet)
router.register('api/v0/teachers', TeachersViewSet)

urlpatterns = router.urls