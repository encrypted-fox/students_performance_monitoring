from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('terms', TermsViewSet)
router.register('marks', MarksViewSet)
router.register('control_types', ControlTypesViewSet)
router.register('records', RecordsViewSet)

urlpatterns = router.urls