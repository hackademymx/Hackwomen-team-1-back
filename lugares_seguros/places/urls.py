from django.urls import URLPattern, path

from .views import PlaceAPIDeleteView
from places import views
from .views import PlaceAPIView

urlpatterns = [
    path('', PlaceAPIView.as_view()),
    path('places/', PlaceAPIDeleteView.as_view()),
]
