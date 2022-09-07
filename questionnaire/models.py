from django.db import models
from django.urls import reverse
from fitapp.models import UserModel


class Questions(models.Model):
    question = models.TextField("Question")

    def __str__(self):
        return self.question


class Answers(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse("answer-update", kwargs={"pk": self.pk})

    def __str__(self):
        return (
            f"User {self.user} has answered {self.answer} to question {self.question}."
        )
