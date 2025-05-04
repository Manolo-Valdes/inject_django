from django.urls import path
from .views import MyView

urlpatterns = [
    path('message/', MyView.as_view(), name='my_view'),
]
