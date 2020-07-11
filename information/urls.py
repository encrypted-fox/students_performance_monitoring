from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)
router.register('records', RecordsViewSet)
router.register('retakes', RetakesViewSet)

urlpatterns = router.urls
