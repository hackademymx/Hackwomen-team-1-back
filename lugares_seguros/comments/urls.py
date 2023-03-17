from django.urls import path
from .views import CommentView
from .views import CommentAPIUpdateView


urlpatterns = [
    path('', CommentView.as_view())
    ]

urlpatterns = [
    path('<int:id>/update/', CommentAPIUpdateView.as_view(), name='update')
] 