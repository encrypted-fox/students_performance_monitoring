from rest_framework import routers
from django.urls import path

from .views import *

router = routers.DefaultRouter()

router.register('start_years', StartYearsViewSet)
router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)
router.register('list_excellent_users', ListExcellentStudents, basename="excellent_user")
urlpatterns = router.urls
