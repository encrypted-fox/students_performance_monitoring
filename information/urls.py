from rest_framework import routers
from django.urls import path

from .views import *

router = routers.DefaultRouter()

router.register('start_years', StartYearsViewSet)
router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)

urlpatterns = router.urls

urlpatterns += path('list_excellent_students', ListAllStudentsWithExcellentMarks.as_view(), name='list_excellent_students')