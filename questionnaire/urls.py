from django.urls import path
from django.views.generic.base import TemplateView

# from .views import QuestionnaireView
from .views import QuestionnaireView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="questionnaire/instructions.html"),
        name="instructions",
    ),
    # path("question/", QuestionnaireView.as_view(), name="questionnaire"),
    # path("question/<int:pk>/", CreateAnswerView.as_view(), name="answer-add"),
    # ANTOINE
    path(
        "question/<int:questionaire_pk>/<int:question>",
        QuestionnaireView.as_view(),
        name="questionnaire",
    ),
]
