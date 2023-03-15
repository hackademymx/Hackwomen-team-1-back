from django.urls import path
from .views import ComentView

urlpatterns=[ 
    path('', ComentView.as_view())
]