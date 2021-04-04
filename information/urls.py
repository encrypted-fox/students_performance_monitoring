from rest_framework import routers
from django.urls import url

from .views import *

router = routers.DefaultRouter()

router.register('start_years', StartYearsViewSet)
router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)

urlpatterns = router.urls

urlpatterns.append(url('list_excellent_students/', ListExcellentStudents.asView(), name='list_excellent_students'))