from django.urls import path, include

urlpatterns = [
    path('', include("ads.urls.Ad")),
    path('', include("ads.urls.Selection")),
    path('', include("ads.urls.Cat")),
    path('user/', include("users.urls.user")),
    path('', include("users.urls.loc"))
    ]

