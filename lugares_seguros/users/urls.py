from django.urls import path
from .views import RegisterUserView, LoginUserView
from .views import RegisterUserAPIUpdateView


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),
]

urlpatterns = [
    path('<int:id>/update/', RegisterUserAPIUpdateView.as_view(), name='update')
] 