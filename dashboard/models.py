from django.db import models
from fitapp.models import UserModel


class StartDate(models.Model):
    """
    The StartDate model stores a new date for the user's start date.

    :param auto_now_add=True: Automatically assigns the value of the field to
                              the current date when the object is first
                              recorded.
    :return: The date the user joined.
    """

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
        help_text="The current user",
    )

    start_date = models.DateField(
        auto_now_add=True, help_text="The date the user started using the app."
    )

    def __str__(self):
        return f"{self.user} - {self.start_date.strftime('%Y-%m-%d')}"
