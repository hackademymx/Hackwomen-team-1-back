from django.urls import URLPattern, path

from .views import PlaceAPIDeleteView
from places import views

urlpatterns= [
    path('places/',PlaceAPIDeleteView.as_view()),   
]

from .views import PlaceAPIView


urlpatterns = [
    path('', PlaceAPIView.as_view())
    ]

