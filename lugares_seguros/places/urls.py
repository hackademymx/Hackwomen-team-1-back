from django.urls import URLPattern, path
from .views import PlaceAPIView
from .views import PlaceAPIUpdateView


urlpatterns = [
    path('', PlaceAPIView.as_view())
    ]


urlpatterns = [
    path('<int:id>/update/', PlaceAPIUpdateView.as_view(), name='update')
] 