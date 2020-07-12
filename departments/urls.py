from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('departments', DepartmentsViewSet)
router.register('subjects', SubjectsViewSet)
router.register('subject_blocks', SubjectBlocksViewSet)

urlpatterns = router.urls
