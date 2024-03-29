from rest_framework import routers

from .views import *
from . import views

router = routers.DefaultRouter()

router.register('start_years',                              StartYearsViewSet)
router.register('terms',                                    TermsViewSet)
router.register('marks',                                    MarksViewSet)
router.register('control_types',                            ControlTypesViewSet)
router.register('list_students_with_more_5',                ListStudentsWithMore5,              basename="students_with_more_5")
router.register('list_students_with_more_4',                ListStudentsWithMore4,              basename="students_with_more_4")
router.register('list_students_with_more_3',                ListStudentsWithMore3,              basename="students_with_more_3")
router.register('list_students_with_more_2',                ListStudentsWithMore2,              basename="students_with_more_2")
router.register('list_students_with_more_pass',             ListStudentsWithMorePass,           basename="students_with_more_pass")
router.register('list_students_with_more_not_pass',         ListStudentsWithMoreNotPass,        basename="students_with_more_not_pass")
router.register('list_students_with_more_not_appointed',    ListStudentsWithMoreNotAppointed,   basename="students_with_more_not_appointed")
router.register('list_students_only_with_more_then_2',      ListStudentsOnlyWithMoreThen2,      basename="students_only_with_more_then_2")
router.register('list_students_only_with_more_then_3',      ListStudentsOnlyWithMoreThen3,      basename="students_only_with_more_then_3")
router.register('list_students_with_less_3',                ListStudentsWithLess3,              basename="students_with_less_3")
router.register('list_students_with_less_2',                ListStudentsWithLess2,              basename="students_with_less_2")
router.register('list_students_with_one_5',                 ListStudentsWithOne5,               basename="students_with_one_5")
router.register('list_students_with_one_4',                 ListStudentsWithOne4,               basename="students_with_one_4")
router.register('list_students_with_one_3',                 ListStudentsWithOne3,               basename="students_with_one_3")
router.register('list_students_with_one_2',                 ListStudentsWithOne2,               basename="students_with_one_2")
router.register('list_students_with_one_pass',              ListStudentsWithOnePass,            basename="students_with_one_pass")
router.register('list_students_with_one_not_pass',          ListStudentsWithOneNotPass,         basename="students_with_one_not_pass")
router.register('list_students_with_one_not_appointed',     ListStudentsWithOneNotAppointed,    basename="students_with_one_not_appointed")
router.register('list_students_only_with_5',                ListStudentsOnlyWith5,              basename="students_only_with_5")
router.register('list_students_only_with_4',                ListStudentsOnlyWith4,              basename="students_only_with_4")
router.register('list_students_only_with_3',                ListStudentsOnlyWith3,              basename="students_only_with_3")
router.register('list_students_only_with_2',                ListStudentsOnlyWith2,              basename="students_only_with_2")
router.register('list_students_only_with_pass',             ListStudentsOnlyWithPass,           basename="students_only_with_pass")
router.register('list_students_only_with_not_pass',         ListStudentsOnlyWithNotPass,        basename="students_only_with_not_pass")
router.register('list_students_only_with_not_appointed',    ListStudentsOnlyWithNotAppointed,   basename="students_only_with_not_appointed")
router.register('list_students_with',                       ListStudentsWith,                   basename="students_with") 


urlpatterns = router.urls
