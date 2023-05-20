from rest_framework import routers
from ads.views import *

router = routers.SimpleRouter()
router.register('ads', AdViewSet)

urlpatterns = router.urls
