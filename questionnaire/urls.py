from django.urls import path
from django.views.generic.base import TemplateView

# from .views import QuestionnaireView
from .views import CreateAnswerView, QuestionnaireView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="questionnaire/instructions.html"),
        name="instructions",
    ),
    path("form/", QuestionnaireView.as_view(), name="questionnaire"),
    path("create/", CreateAnswerView.as_view(), name="answer-add"),
    # path("question/<int:pk>/", CreateAnswerView.as_view(), name="answer-add"),
]
