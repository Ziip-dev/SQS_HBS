# from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import QuestionnaireForm
from .models import Answer, Questionnaire

# from fitapp.utils import is_integrated


# class QuestionnaireView(FormView):
#     template_name = "questionnaire/questionnaire.html"
#     form_class = Questionnaire
#     success_url = reverse_lazy("answer-add")

#     def form_valid(self, form):
#         # form.save()
#         return super().form_valid(form)

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


# class QuestionnaireView(CreateView):
#     template_name = "questionnaire/questionnaire.html"
#     success_url = reverse_lazy("questionnaire")
#     # fields = ["question", "answer"]
#     # context_object_name = "answers"

#     def get_success_url(self, **kwargs):
#         pass


# ANTOINE
class QuestionnaireView(CreateView):
    model = Answer
    form_class = QuestionnaireForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questionnaire = Questionnaire.get(pk=kwargs["questionaire_pk"])

        # django fait de la magie et fout un question_set dans le questionnaire si y'a des foreign key Question->Questionnaire
        # https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
        context["question"] = questionnaire.question_set[kwargs["question"]]
        return context
