from rest_framework import routers
from django.urls import path

from .views import *

router = routers.DefaultRouter()

router.register('start_years', StartYearsViewSet)
router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)
router.register('list_excellent_students', ListExcellentStudents, basename="excellent_user")
router.register('list_good_students_with_more_5', ListGoodStudentsWithMore5, basename="good_students_with_more_5")
router.register('list_good_studetns_with_more_4', ListGoodStudentsWithMore4, basename="ood_studetns_with_more_4")
router.register('list_students_only_with_more_then_3', ListStudentsOnlyWithMoreThen3, basename="students_only_with_more_then_3")
router.register('list_students_only_with_more_then_2', ListStudentsOnlyWithMoreThen2, basename="students_only_with_more_then_2")
router.register('list_students_with_2', ListStudentsWith2, basename="students_with_2")
router.register('list_students_only_with_2', ListStudentsOnlyWith2, basename="students_only_with_2")
router.register('list_students_with', ListStudentsWith, basename="students_with")


urlpatterns = router.urls
