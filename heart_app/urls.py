from django.urls import path
from heart_app import views

urlpatterns = [
    path("", views.home, name="home"),
]