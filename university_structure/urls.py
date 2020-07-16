from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('faculties', FacultiesViewSet)
router.register('departments', DepartmentsViewSet)
router.register('specializations', SpecializationsViewSet)
router.register('educational_programs', EducationProgramsViewSet)
router.register('groups', GroupsViewSet)

urlpatterns = router.urls
