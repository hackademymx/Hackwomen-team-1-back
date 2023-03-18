from django.urls import URLPattern, path
from .views import PlaceAPIView
from .views import PlaceAPIUpdateDeleteView


urlpatterns = [
    path('', PlaceAPIView.as_view()),
    path('<int:id>/', PlaceAPIUpdateDeleteView.as_view())
    ]