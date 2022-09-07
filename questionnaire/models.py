from django.db import models
from django.urls import reverse
from fitapp.models import UserModel

# class Questions(models.Model):
#     question = models.TextField("Question")


# ANTOINE
class Questionnaire(models.Model):
    questionaire_pk = models.IntegerField()

    def __str__(self):
        return self.questionaire_pk


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
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.answer
