from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import QuestionnaireForm
from .models import Answer, Question, Questionnaire


class QuestionnaireView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = QuestionnaireForm
    template_name = "questionnaire/questionnaire.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questionnaire = Questionnaire.objects.get(pk=self.kwargs["questionnaire_pk"])
        context["question"] = questionnaire.question_set.all()[self.kwargs["question"]]
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = Question.objects.get(pk=self.kwargs["question"] + 1)
        return super().form_valid(form)

    def get_success_url(self):
        question_id = self.kwargs["question"] + 1
        questionnaire_pk = self.kwargs["questionnaire_pk"]
        max_question = Question.objects.filter(
            questionnaire_id=questionnaire_pk
        ).count()

        # Return to questionnaire with the next question
        if question_id < max_question:
            return reverse_lazy(
                "questionnaire",
                kwargs={"questionnaire_pk": questionnaire_pk, "question": question_id},
            )

        # Return to home when all the questions have been answered
        elif question_id == max_question:
            return reverse_lazy("home")
