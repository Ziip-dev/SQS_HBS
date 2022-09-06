from django.shortcuts import redirect, render
from fitapp.utils import is_integrated


def questionnaire(request, question_number):
    if request.method == "GET":
        if request.user.is_authenticated and is_integrated(request.user):

            context = {
                "question_number": question_number,
                "question": "This is a question from the questionnaire",
            }

            return render(request, "questionnaire/questionnaire.html", context)

        else:
            redirect("login")

    elif request.method == "POST":
        pass
