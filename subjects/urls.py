from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('subjects', SubjectsViewSet)
router.register('subject_blocks', SubjectBlocksViewSet)
router.register('subjects_subject_blocks', SubjectsSubjectBlocksViewSet)
router.register('records', RecordsViewSet)

urlpatterns = router.urls
