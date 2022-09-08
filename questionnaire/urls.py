from django.urls import path
from django.views.generic.base import TemplateView

from .views import QuestionnaireView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="questionnaire/instructions.html"),
        name="instructions",
    ),
    path(
        "question/<int:questionnaire_pk>/<int:question>",
        QuestionnaireView.as_view(),
        name="questionnaire",
    ),
]
