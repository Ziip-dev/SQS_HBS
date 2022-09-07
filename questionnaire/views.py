# from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from .forms import Questionnaire
from .models import Answers

# from fitapp.utils import is_integrated


class QuestionnaireView(FormView):
    """
    View to only render the questionnaire form.
    It is then posted to the CreateAnswerView which handles writing in the database.
    """

    template_name = "questionnaire/questionnaire.html"
    form_class = Questionnaire
    success_url = reverse_lazy("answer-add")

    def form_valid(self, form):
        # form.save()
        return super().form_valid(form)

    # def get(self, request, pk):
    #     if request.user.is_authenticated and is_integrated(request.user):

    #         question = get_object_or_404(Questions, pk=pk)

    #         # Create context dictionary for the template
    #         context = {
    #             "question": question,
    #         }

    #         return render(request, self.template_name, context)

    #     else:
    #         redirect("login")

    # def post(self, request):
    #     pass


class CreateAnswerView(CreateView):
    """
    Write the posted form answers to the database.
    """

    model = Answers
    form_class = Questionnaire
    template_name = "questionnaire/questionnaire.html"
    success_url = reverse_lazy("answer-add")
    # fields = ["question", "answer"]
    # context_object_name = "answers"
