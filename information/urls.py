from rest_framework import routers
from django.urls import path

from .views import *
from . import views

router = routers.DefaultRouter()

router.register('start_years', StartYearsViewSet)
router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)

urlpatterns = router.urls

urlpatterns.append(path('list_excellent_students/', ListExcellentStudents.asView())