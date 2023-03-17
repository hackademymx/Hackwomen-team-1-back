from django.urls import URLPattern, path
from .views import PlaceAPIView
from .views import PlaceAPIUpdateDeleteView


urlpatterns = [
    path('', PlaceAPIView.as_view()),
    path('', PlaceAPIUpdateDeleteView.as_view())
    ]