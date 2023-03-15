from django.urls import URLPattern, path
<<<<<<< HEAD
from .views import PlaceAPIDeleteView
from places import views

urlpatterns= [
    path('places/',PlaceAPIDeleteView.as_view()),   
]
=======
from .views import PlaceAPIView


urlpatterns = [
    path('', PlaceAPIView.as_view())
    ]
>>>>>>> b90613e8ab3811348bf34a27e57a3f3b724c9d1f
