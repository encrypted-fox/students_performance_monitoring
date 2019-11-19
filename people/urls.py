from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('students', StudentsViewSet)
router.register('teachers', TeachersViewSet)

urlpatterns = router.urls