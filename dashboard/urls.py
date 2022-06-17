# dashboard/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("subscription/", views.fitbit_subscription, name="subscription"),
]
