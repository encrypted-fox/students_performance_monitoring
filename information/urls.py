from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('start_years', StartYearsViewSet)
router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)

urlpatterns = router.urls
