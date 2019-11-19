from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('faculties', FacultiesViewSet)
router.register('educational_programs', EducationalProgramsViewSet)
router.register('specializations', SpecializationsViewSet)
router.register('groups', GroupsViewSet)

urlpatterns = router.urls