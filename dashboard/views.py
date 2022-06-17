# dashboard/views.py

from django.shortcuts import redirect, render
from fitapp.decorators import fitbit_integration_warning


@fitbit_integration_warning(msg="Integrate your account with Fitbit!")
def home(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/home.html")

    else:
        return redirect("login")
