# dashboard/views.py

from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from fitapp.decorators import fitbit_integration_warning
from fitapp.models import TimeSeriesData


@fitbit_integration_warning(msg="Integrate your account with Fitbit!")
def home(request):
    if request.user.is_authenticated:
        # retrieve user data from database
        # now = datetime.datetime.now()  # parse to "YYYY-MM-DD"
        tsds = TimeSeriesData.objects.filter(user=request.user, date="2022-06-29")

        # for tsd in TimeSeriesData.objects.filter(user=self.user, date=date):

        # TimeSeriesData.objects.filter(user=self.user, date=date).count(),

        # activities = TimeSeriesDataType.activities

        return render(request, "dashboard/home.html", {"tsds": tsds})

    else:
        return redirect("login")


def service_worker(request):
    sw_path = Path(settings.STATIC_ROOT, "sw.js")
    response = HttpResponse(open(sw_path).read(), content_type="application/javascript")
    return response
