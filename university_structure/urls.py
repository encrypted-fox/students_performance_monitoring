from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('api/v0/faculties', FacultiesViewSet)
router.register('api/v0/educational_programs', EducationalProgramsViewSet)
router.register('api/v0/specializations', SpecializationsViewSet)
router.register('api/v0/groups', GroupsViewSet)

urlpatterns = router.urls