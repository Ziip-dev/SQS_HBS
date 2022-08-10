from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="dashboard/login.html"),
        name="login",
    ),
    path("sw.js", views.service_worker),
    path(
        "offline/",
        TemplateView.as_view(template_name="dashboard/offline.html"),
        name="offline",
    ),
]
