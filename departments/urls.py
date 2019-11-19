from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('api/v0/departments', DepartmentsViewSet)
router.register('api/v0/subjects', SubjectsViewSet)
router.register('api/v0/subject_blocks', SubjectBlocksViewSet)
router.register('api/v0/subjects_subject_blocks', SubjectsSubjectBlocksViewSet)


urlpatterns = router.urls