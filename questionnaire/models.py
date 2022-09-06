from django.db import models
from fitapp.models import UserModel


class Questions(models.Model):
    # 1 table avec une question par ligne identifiée par son numéro en pk
    question = models.TextField


class Answers(models.Model):

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
        help_text="The current user",
    )
