# dashboard/views.py

import random
from datetime import date, timedelta
from pathlib import Path

from django.conf import settings
from django.db.models import IntegerField, Sum
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.shortcuts import redirect, render
from fitapp.decorators import fitbit_integration_warning
from fitapp.models import TimeSeriesData
from fitapp.utils import is_integrated

from .models import StartDate


@fitbit_integration_warning(
    msg="Connectez-vous à Fitbit à l'aide des identifiants fournis"
)
def home(request):
    """
    The home view renders the home page template.
    It checks if the user is authenticated, stores the start date at the first login,
    and retrieves the user's physical activity data.
    It then parses the retrieved data and pass it to the home template.

    :return: The home page template or the login template.
    """
    if request.user.is_authenticated and is_integrated(request.user):
        #  Store the experiment start date after the first login and redirect to questionnaire
        if not StartDate.objects.filter(user=request.user).exists():
            StartDate(user=request.user).save()
            # redirect to self-efficacy questionnaire

        # Retrieve user start date as datetime object and compute end_date
        start_date = StartDate.objects.get(user=request.user).start_date
        end_date = start_date + timedelta(days=15)
        print("""
              start_date = {start_date}
              today      = {date.today()}
              end_date   = {end_date}
              """)
        # if date.today() == end_date:
        # redirect to self-efficacy questionnaire

        # Retrieve and parse user PA data per week (for the 2-week steam graph)
        # retrieve necessary user's physical activity (PA) data from database
        wanted_resources = ["minutesFairlyActive", "minutesVeryActive"]
        user_PA_data = TimeSeriesData.objects.filter(
            user=request.user,
            resource_type__resource__in=wanted_resources,
            date__gte=start_date,
        )

        # sum minutesFairlyActive and minutesVeryActive values per day
        aggregated_PA_data = (
            user_PA_data.values("date")
            .annotate(minutesActive=Sum(Cast("value", IntegerField())))
            .order_by("date")
        )

        # separate PA data into lists of 7 days
        weekly_PA_data = [
            aggregated_PA_data[d: d + 7]
            for d in range(0, aggregated_PA_data.count(), 7)
        ]

        # retrieve the first two weeks of the experiment
        first_week_started = True if len(weekly_PA_data) >= 1 else False
        second_week_started = True if len(weekly_PA_data) >= 2 else False

        if first_week_started:
            week_1_PA_data = weekly_PA_data[0]

        if second_week_started:
            week_2_PA_data = weekly_PA_data[1]

        # isolate PA values as lists, and complete with 0 for the remaining days of the week
        if first_week_started:
            week_1_PA_values = [d.get("minutesActive") for d in week_1_PA_data] + [
                0
            ] * (7 - week_1_PA_data.count())
        if second_week_started:
            week_2_PA_values = [d.get("minutesActive") for d in week_2_PA_data] + [
                0
            ] * (7 - week_2_PA_data.count())

        # Pick randomly an informative message about PA
        messages_path = Path(settings.STATIC_ROOT,
                             "dashboard", "PA_messages.txt")
        lines = open(messages_path).read().splitlines()
        message_PA = random.choice(lines)

        # Create the context dictionary with the data to be sent to the template
        context = {
            "PA_1": week_1_PA_values if first_week_started else [0] * 7,
            "PA_2": week_2_PA_values if second_week_started else [0] * 7,
            "PA_message": message_PA,
        }

        return render(request, "dashboard/home.html", context)

    elif request.user.is_authenticated and not is_integrated(request.user):
        return render(request, "dashboard/integration.html")

    else:
        return redirect("login")


def service_worker(request):
    sw_path = Path(settings.STATIC_ROOT, "sw.js")
    response = HttpResponse(open(sw_path).read(),
                            content_type="application/javascript")
    return response
