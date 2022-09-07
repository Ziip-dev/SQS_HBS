from django.forms import ChoiceField, ModelForm, RadioSelect

from .models import Answers


class QuestionnaireForm(ModelForm):
    CHOICES = [
        (1, "désapprouve fortement"),
        (2, "désapprouve un peu"),
        (3, "n'approuve ni ne désapprouve"),
        (4, "approuve un peu"),
        (5, "approuve fortement"),
    ]

    answers = ChoiceField(choices=CHOICES, widget=RadioSelect())

    class Meta:
        model = Answers
        fields = ["question", "answer"]
