from django.db import models
from fitapp.models import UserModel


class Questionnaire(models.Model):
    """
    Model containing every questions.
    Linked by the Question.questionnaire ForeignKey in each question.
    """

    questionnaire_pk = models.IntegerField()

    def __str__(self):
        return str(self.questionnaire_pk)


class Question(models.Model):
    question = models.TextField()
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - question {self.question.id} ({self.created})"
