# dashboard/views.py

from pathlib import Path

from birdseye import eye
from django.conf import settings
from django.db.models import IntegerField, Sum
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.shortcuts import redirect, render
from fitapp.decorators import fitbit_integration_warning
from fitapp.models import TimeSeriesData

from .models import StartDate


@fitbit_integration_warning(
    msg="Connectez-vous à Fitbit à l'aide des identifiants fournis"
)
@eye
def home(request):
    if request.user.is_authenticated:
        #  If not already present, store the experiment start date after the first login
        if not StartDate.objects.filter(user=request.user).exists():
            StartDate(user=request.user).save()

        # Retrieve and parse user data for the 2-week steam graph
        # start date as datetime object
        from datetime import timedelta

        start_date = StartDate.objects.get(user=request.user).start_date - timedelta(
            days=13
        )

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
            aggregated_PA_data[d : d + 7]
            for d in range(0, aggregated_PA_data.count(), 7)
        ]

        # retrieve the first two weeks of the experiment
        week_1_PA_data = weekly_PA_data[0]
        # TODO là va y avoir un soucis d'OOB pendant la première semaine d'XP...
        week_2_PA_data = weekly_PA_data[1]

        # isolate PA values as lists, and complete with 0 for the remaining days of the week
        week_1_PA_values = [d.get("minutesActive") for d in week_1_PA_data] + [0] * (
            7 - week_1_PA_data.count()
        )
        week_2_PA_values = [d.get("minutesActive") for d in week_2_PA_data] + [0] * (
            7 - week_2_PA_data.count()
        )

        print(
            f"""
              {week_1_PA_values}
              {week_2_PA_values}
              """
        )

        # create context dictionary with one entry per week
        context = {
            "PA_1": week_1_PA_values,
            "PA_2": week_2_PA_values,
        }

        return render(request, "dashboard/home.html", context)

    else:
        return redirect("login")


def service_worker(request):
    sw_path = Path(settings.STATIC_ROOT, "sw.js")
    response = HttpResponse(open(sw_path).read(), content_type="application/javascript")
    return response
