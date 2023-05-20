from rest_framework import routers
from ads.views import *

router = routers.SimpleRouter()
router.register('cat', CatViewSet)

urlpatterns = router.urls
