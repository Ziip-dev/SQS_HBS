======================================================
Self-Quantification System for Health Behavior Support
======================================================

This is an experimental PhD project that personalises interactions in human-computer interfaces based on personality traits (see `Big Five personality traits <https://en.wikipedia.org/wiki/Big_Five_personality_traits>`_).

The experiment aimed to investigate if using an individualised app could improve the effectiveness of supporting physical activity behaviour change for users with high neuroticism.

This project provides a customised mobile app for users with high neuroticism levels using an interdisciplinary approach that combines behavioural psychology and human-computer interactions.


GETTING STARTED
===============

Requirements
------------

- :code:`git`
- :code:`python 3` (tested with 3.10)
- :code:`poetry` (optional but recommended)


For production
--------------

To deploy on a server, the easiest solution is by far using `Caprover PaaS <https://caprover.com/>`_.

1. Clone the project repository locally: ::

    git clone https://github.com/Ziip-dev/SQS_HBS.git

2. The app needs to be deployed twice in two different instances: one for the webserver, and one for celery (which have a different entry point). This is the method actually used by Heroku for such cases.

   - Hence, set up 2 server side apps (see `Caprover documentation <https://caprover.com/docs/get-started.html>`_ on Caprover.

   - Navigate to the first app, go to :code:`DEPLOYMENT` tab, and edit the :code:`captain-definition` path to :code:`./captain-definition-webserver`.

   - Then do the same for the second instance with :code:`./captain-definition-celery`

3. Caprover should now be able to deploy the app to its dedicated instance using the correct entry point (do this twice, for the webserver and for celery): ::

    caprover deploy

4. Create a :TODO:

5. Finally, use the Django admin site to create users as needed.



For development
~~~~~~~~~~~~~~~

Clone both project repositories::

    git clone https://github.com/Ziip-dev/SQS_HBS.git
    git clone https://github.com/Ziip-dev/django-fitbit.git

Create a python virtual environment::

    poetry env use /path/to/python3.10

Install dependencies::

    poetry install


Deployment
----------

- dockerisation
- collectstatic to run on server


Docker
------

1. Run the helper script to automatically build the image and execute the container:

   ::

       $ ./start_container.sh


Software stack
==============

This web app is configured as a PWA so it can be installed on mobile phones, which was the aim of the experiment.
It is built around:

- **Django** :: to leverage built-in user authentication and built-in class-based generic views.

- **`django-fitbit <https://github.com/Ziip-dev/django-fitbit>`_** :: a django app that I have updated to manage Fitbit authentication, API requests, and database writes.

- **Bulma** :: to speed up the frontend development with ready-to-use components that can be easily combined to build a responsive interface.

- **PostgreSQL** :: for time series data management, which require simultaneous reads and writes for multiple users.

- **RabbitMQ** :: for job queuing, e.g. pending Fitbit Web API requests, database read/write, etc.

- **Celery** :: concurrent task execution, e.g. to simultaneously retrieve multiple users data from the Fitbit Web API.



LICENSE
=======

Distributed under the terms of the `GNU AGPL v3`_.

.. _GNU AGPL v3: https://github.com/Ziip-dev/SQS_HBS/blob/main/LICENSE


ISSUES
======

If you encounter any problems, please `file an issue`_ along with a
detailed description.

.. _file an issue: https://github.com/Ziip-dev/SQS_HBS/issues


ROADMAP
=======

- *completed*


CHANGELOG
=========

- Integrate information messages on the emotional consequences of PA.

- IRL phone test.

- Set up the user dashboard.

- Turn into a PWA.

- Integrate Celery to take advantage of the asynchronous tasks already written in the fitapp project, change the backend database to manage concurrency effectively and switch to an execution pool based on green threads.

- Switch to a monitoring system based on issues + pull requests, the README will become bigger than the code otherwise...

- Solving the problem of requests from different users:

    - declare a Server App on my Fitbit account.

    - test whether I can retrieve non-intraday data for :code:`test-user-1` AND :code:`test-user-2`.

- Get the :code:`fitapp` django app working now that I have update it and correctly declared.

  - set up user authentication to access fitbit views.

      - :code:`livereload` server for fast development of templates

        --> cancelled, too many bugs during live reloads.

      - :code:`WhiteNoise` setup for static files serving.


DEBUG NOTES
===========

CLI
---

- refresh expired authentication tokens: :code:`./manage.py refresh_tokens -v 3`

- refresh even non-expired tokens: :code:`./manage.py refresh_tokens --all`

- del users with invalid refresh tokens: :code:`./manage.py refresh_tokens --deauth`

  --> :code:`--deauth` removes :code:`UserFitbit`
