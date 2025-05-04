from django.urls import path
from .views import hello_world, MyView

urlpatterns = [
    path('hello/', hello_world),
    path('message/', MyView.as_view(), name='my_view'),
]
