from rest_framework import routers
from django.urls import path

from .views import *

router = routers.DefaultRouter()

router.register('start_years', StartYearsViewSet)
router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)
router.register('list_students_with_more_5',            ListStudentsWithMore5,              basename="students_with_more_5")
router.register('list_students_with_more_4',            ListStudentsWithMore4,              basename="students_with_more_4")
router.register('list_students_with_more_3',            ListStudentsWithMore3,              basename="students_with_more_3")
router.register('list_students_with_more_2',            ListStudentsWithMore2,              basename="students_with_more_2")
router.register('list_students_only_with_more_then_2',  ListStudentsOnlyWithMoreThen2,      basename="students_only_with_more_then_2")
router.register('list_students_only_with_more_then_3',  ListStudentsOnlyWithMoreThen3,      basename="students_only_with_more_then_3")
router.register('list_students_with_less_3',            ListStudentsWithLess3,              basename="students_with_less_3")
router.register('list_students_with_less_2',            ListStudentsWithLess2,              basename="students_with_less_2")
router.register('list_students_with_one_3',             ListStudentsWithOne3,               basename="students_with_one_3")
router.register('list_students_with_one_2',             ListStudentsWithOne2,               basename="students_with_one_2")
router.register('list_students_with_one_not_appointed', ListStudentsWithOneNotAppointed,    basename="students_with_one_not_appointed")
router.register('list_students_only_with_5',            ListStudentsOnlyWith5,              basename="students_only_with_5")
router.register('list_students_only_with_4',            ListStudentsOnlyWith4,              basename="students_only_with_4")
router.register('list_students_only_with_3',            ListStudentsOnlyWith3,              basename="students_only_with_3")
router.register('list_students_only_with_2',            ListStudentsOnlyWith2,              basename="students_only_with_2")
router.register('list_students_only_with_appointed',    ListStudentsOnlyWithNotAppointed,   basename="students_only_with_not_appointed")
router.register('list_students_with',                   ListStudentsWith,                   basename="students_with")


urlpatterns = router.urls
