from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('api/v0/terms', TermsViewSet)
router.register('api/v0/marks', MarksViewSet)
router.register('api/v0/control_types', ControlTypesViewSet)
router.register('api/v0/records', RecordsViewSet)


urlpatterns = router.urls