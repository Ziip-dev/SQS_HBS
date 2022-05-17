import fitapp
import simplejson as json
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse

# trunk-ignore(flake8/F401)
from fitapp.models import TimeSeriesData, TimeSeriesDataType, UserFitbit
from fitbit.exceptions import (
    HTTPConflict,
    HTTPForbidden,
    HTTPServerError,
    HTTPUnauthorized,
)


# TEMP
#########################################################################
# for testing with dashboard.views.fitbit_subscription
# with password stored in .env file
def get_setting(name, use_defaults=False):
    """Retrieves the specified setting from the settings file.

    If the setting is not found, raise an ImproperlyConfigured exception.
    """
    if hasattr(settings, name):
        return _verified_setting(name)
    msg = f"{name} must be specified in your settings"
    raise ImproperlyConfigured(msg)


def _verified_setting(name):
    result = getattr(settings, name)
    if name == "FITAPP_SUBSCRIPTIONS":
        # Check that the subscription list is valid
        try:
            items = result.items()
        except AttributeError:
            msg = "{} must be a dict or an OrderedDict".format(name)
            raise ImproperlyConfigured(msg)
        # Only make one query, which will be cached for later use
        all_tsdt = list(TimeSeriesDataType.objects.all())
        for cat, res in items:
            tsdts = list(filter(lambda t: t.get_category_display() == cat, all_tsdt))
            if not tsdts:
                msg = "{} is an invalid category".format(cat)
                raise ImproperlyConfigured(msg)
            all_cat_res = set(map(lambda tsdt: tsdt.resource, tsdts))
            if set(res) & all_cat_res != set(res):
                msg = "{0} resources are invalid for the {1} category".format(
                    list(set(res) - (set(res) & all_cat_res)), cat
                )
                raise ImproperlyConfigured(msg)
    return result


#########################################################################


def make_response(code=None, objects=[]):
    """Helper method to generate a response"""

    data = {
        "meta": {"total_count": len(objects), "status_code": code},
        "objects": objects,
    }
    return HttpResponse(json.dumps(data))


def retrieve_fitbit_data(
    user, category, resource, base_date=None, end_date=None, period=None
):
    """Function adapted from fitapp.views.get_data so it can be called directly
    from the dashboard.views.fitbit_subscription view instead of an AJAX request.

    This function retrieves the user's data from Fitbit, either from a range of
    dates, with specific start and end days, or from a time period ending on a
    specific date.

    The two first parameters, category and resource, determine which type of data
    to retrieve. The category parameter can be one of: foods, activities,
    sleep, and body. The resource parameter should be the rest of
    https://dev.fitbit.com/build/reference/web-api/activity-timeseries/get-activity-timeseries-by-date/#Resource-Options

    To retrieve a specific time period, two parameters are used:

        :period: A string describing the time period, ending on *base_date*,
            for which to retrieve data - one of '1d', '7d', '30d', '1w', '1m',
            '3m', '6m', '1y', or 'max.
        :base_date: The last date (in the format 'yyyy-mm-dd') of the
            requested period. If not provided, then *base_date* is
            assumed to be today.

    To retrieve a range of dates, two parameters are used:

        :base_date: The first day of the range, in the format 'yyyy-mm-dd'.
        :end_date: The final day of the range, in the format 'yyyy-mm-dd'.

    The response body contains a JSON-encoded map with two items:

        :objects: an ordered list (from oldest to newest) of daily data
            for the requested period. Each day is of the format::

               {'dateTime': 'yyyy-mm-dd', 'value': 123}

           where the user has *value* on *dateTime*.

        :meta: a map containing two things: the *total_count* of objects, and
            the *status_code* of the response.

    When everything goes well, the *status_code* is 100 and the requested data
    is included. However, there are a number of things that can 'go wrong'
    with this call. For each type of error, we return an empty data list with
    a *status_code* to describe what went wrong on our end:

        :100: OK - Response contains JSON data.
        :101: User is not logged in.
        :102: User is not integrated with Fitbit.
        :103: Fitbit authentication credentials are invalid and have been
            removed.
        :104: Invalid input parameters. Either *period* or *end_date*, but not
            both, must be supplied. *period* should be one of [1d, 7d, 30d,
            1w, 1m, 3m, 6m, 1y, max], and dates should be of the format
            'yyyy-mm-dd'.
        :105: User exceeded the Fitbit limit of 150 calls/hour.
        :106: Fitbit error - please try again soon.
    """

    try:
        resource_type = TimeSeriesDataType.objects.get(
            category=getattr(TimeSeriesDataType, category), resource=resource
        )

    # trunk-ignore(flake8/E722)
    except:
        return make_response(104)

    # Check if the user has a subscribed fitbit integration
    fitapp_subscribe = fitapp.utils.get_setting("FITAPP_SUBSCRIBE")
    if not user.is_authenticated or not user.is_active:
        return make_response(101)
    if not fitapp_subscribe and not fitapp.utils.is_integrated(user):
        return make_response(102)

    # Select the correct endpoint regarding the retrieved parameters
    if period and not end_date:
        form = fitapp.forms.PeriodForm({"base_date": base_date, "period": period})
    elif end_date and not period:
        form = fitapp.forms.RangeForm({"base_date": base_date, "end_date": end_date})
    else:
        # either end_date or period, but not both, must be specified.
        return make_response(104)

    fitbit_data = form.get_fitbit_data()
    if not fitbit_data:
        return make_response(104)

    # À bouger dans une autre fonction
    ### Request data directly from the database if the user is suscribed to automated Fitbit updates.
    # if fitapp_subscribe:
    #     date_range = normalize_date_range(request, fitbit_data)
    #     existing_data = TimeSeriesData.objects.filter(
    #         user=user, resource_type=resource_type, **date_range)
    #     simplified_data = [{'value': d.value, 'dateTime': d.string_date()}
    #                        for d in existing_data]
    #     return make_response(100, simplified_data)

    ### Request data through the API and handle related errors.
    fbuser = UserFitbit.objects.get(user=user)
    try:
        data = fitapp.utils.get_fitbit_data(fbuser, resource_type, **fitbit_data)
    except (HTTPUnauthorized, HTTPForbidden):
        # Delete invalid credentials.
        fbuser.delete()
        return make_response(103)
    except HTTPConflict:
        return make_response(105)
    except HTTPServerError:
        return make_response(106)
    # trunk-ignore(flake8/E722)
    except:
        # Other documented exceptions include TypeError, ValueError,
        # HTTPNotFound, and HTTPBadRequest. But they shouldn't occur, so we'll
        # send a 500 and check it out.
        raise

    return make_response(100, data)


def test_write_user_data():
    # write to BDD

    # TimeSeriesData.objects.create(
    #     user=self.user,
    #     resource_type=TimeSeriesDataType.objects.get(
    #         category=TimeSeriesDataType.activities, resource='steps'),
    #     date=steps[0]['dateTime'],
    #     value=steps[0]['value']
    # )

    # for datum in data:
    #     # Create new record or update existing record
    #     date = parser.parse(datum['dateTime'])
    #     tsd, created = TimeSeriesData.objects.get_or_create(
    #         user=fbuser.user, resource_type=_type, date=date)
    #     tsd.value = datum['value']
    #     tsd.save()

    pass


def test_read_user_data():
    # read from BDD

    # for tsd in TimeSeriesData.objects.filter(user=self.user, date=date):

    # TimeSeriesData.objects.filter(user=self.user, date=date).count(),

    # activities = TimeSeriesDataType.activities

    pass
