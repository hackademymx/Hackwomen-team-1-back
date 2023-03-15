from django.urls import URLPattern, path
from .views import PlaceAPIView


urlpatterns = [
    path('', PlaceAPIView.as_view())
    ]