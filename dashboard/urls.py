from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sw.js", views.service_worker),
    path(
        "offline/",
        TemplateView.as_view(template_name="dashboard/offline.html"),
        name="offline",
    ),
]
