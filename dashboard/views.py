# dashboard/views.py

from datetime import date, datetime, timedelta
from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from fitapp.decorators import fitbit_integration_warning
from fitapp.models import TimeSeriesData

from .models import StartDate

from birdseye import eye


@fitbit_integration_warning(
    msg="Connectez-vous à Fitbit à l'aide des identifiants fournis"
)
@eye
def home(request):
    if request.user.is_authenticated:
        #  If not already present, store the experiment start date after the first login
        if not StartDate.objects.filter(user=request.user).exists():
            StartDate(user=request.user).save()

        # Retrieve the necessary data for the 2-week steam graph
        # start date as datetime object and current day
        start_date = StartDate.objects.get(user=request.user).start_date
        # today = date.today()

        # current week
        # current_week = date - timedelta(days=7)

        # last week
        # last_week =

        tsds = TimeSeriesData.objects.filter(
            user=request.user, date__gte=start_date).order_by("date")

        print("")
        for tsd in tsds:
            print(
                f"    - {tsd.date}: {tsd.user}, {tsd.value} {tsd.resource_type.resource}")
        print("")

        # TODO ok j'ai toute la récupération qui marche bien, plus qu'à parser :D
        # On somme minutesFairlyActive et minutesVeryActive pour avoir
        # le niveau d'AP pour un jour, qu'on passe au template.

        # FIXME pas besoin de passer tout le QuerySet, c'était pour tester.
        context = {
            "tsds": tsds,
        }

        return render(request, "dashboard/home.html", context)

    else:
        return redirect("login")


def service_worker(request):
    sw_path = Path(settings.STATIC_ROOT, "sw.js")
    response = HttpResponse(open(sw_path).read(),
                            content_type="application/javascript")
    return response
