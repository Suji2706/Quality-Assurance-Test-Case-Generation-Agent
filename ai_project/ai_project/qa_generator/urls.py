from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_testcases, name='generate_testcases'),
]
