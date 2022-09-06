from django.urls import path

from . import views

urlpatterns = [
    path("question/<int:question_number>/", views.questionnaire, name="questionnaire")
]
