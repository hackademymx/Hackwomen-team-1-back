from django.urls import URLPattern, path
<<<<<<< HEAD
from .views import PlaceAPIView, PlaceAPIUpdateDeleteView
=======
from .views import PlaceAPIView
from .views import PlaceAPIUpdateDeleteView
>>>>>>> 185d4395d98364163e2b7e9e75e963d09e9c30ad


urlpatterns = [
    path('', PlaceAPIView.as_view()),
<<<<<<< HEAD
    path('<int:id>/', PlaceAPIUpdateDeleteView.as_view()),
]
=======
    path('<int:id>/', PlaceAPIUpdateDeleteView.as_view())
    ]
>>>>>>> 185d4395d98364163e2b7e9e75e963d09e9c30ad
