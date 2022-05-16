# dashboard/views.py

from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from fitapp.decorators import fitbit_integration_warning
from .utils import retrieve_fitbit_data


@fitbit_integration_warning(msg="Integrate your account with Fitbit!")
def home(request):
    if request.user.is_authenticated:

        # on récupère le retours de la requête en JSON
        # {"meta": {"total_count": 1, "status_code": 100}, "objects": [{"dateTime": "2022-04-01", "value": "847"}]}

        # on en extrait les données voulue : la liste correspondant à la clé "objects"
        # [{"dateTime": "2022-04-01", "value": "847"}]

        # on stocke nos données utilisateur dans la BDD
        # test_write_user_data()

        return render(request, "dashboard/home.html")
        
    else:
        return redirect("login")


@csrf_exempt
@require_http_methods(["POST"])
def fitbit_subscription(request):
    # will be https://xp.caprover-root.ocas-phd.fr/subscription/

    # Reveive Fitbit webhook via POST request
    # Locally simulated by a `curl -X POST http://127.0.0.1:7000/subscription/` for now

    # Verify subscriber endpoint
    # --> add code to respond correctly to a verification code (maybe managed by fitapp??)

    # Check X-Fitbit-Signature --> peut-être déjà intégré dans fitapp
    # https://dev.fitbit.com/build/reference/web-api/developer-guide/best-practices/#Subscriber-Security

    # Answer to Fitbit within 5s (see doc)

    # Authenticate the right user (if valid, returns ~User~ object, ~None~ otherwise).
    user = authenticate(username='Anais', password='mamounia31')

    # Fitbit request parameters
    category = 'activities'
    resource = 'minutesSedentary'
    base_date = '2022-04-01'
    period = '1d'

    # Retrieve Fitbit data using a custom utils function based on the
    # fitapp.views.get_data request constructor
    user_data = retrieve_fitbit_data(user, category, resource, base_date=base_date, period=period)


    return user_data