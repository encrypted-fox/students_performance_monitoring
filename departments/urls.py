from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('departments', DepartmentsViewSet)
router.register('subjects', SubjectsViewSet)
router.register('subject_blocks', SubjectBlocksViewSet)
router.register('subjects_subject_blocks', SubjectsSubjectBlocksViewSet)


urlpatterns = router.urls