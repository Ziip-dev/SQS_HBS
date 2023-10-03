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

Production
~~~~~~~~~~

- Caprover PaaS on a production server (not compulsory but strongly recommended)
- A correctly declared server app on Fitbit dev website
- :code:`caprover` CLI
- :code:`git`

Development
~~~~~~~~~~~

- Docker
- Poetry (optional)

Installation and Deployment
---------------------------

For production
~~~~~~~~~~~~~~

To deploy on a production server, the easiest and recommended solution is to use `Caprover PaaS <https://caprover.com/>`_.

1. Clone the project repository locally: ::

    git clone https://github.com/Ziip-dev/SQS_HBS.git

2. The app needs to be deployed twice in two different instances: one for the **webserver**, and one for **celery** (which have different entry points).
   This is the method actually used by Heroku for such cases:

   - Set up 2 server side apps (see `Caprover documentation <https://caprover.com/docs/get-started.html>`_ on Caprover.

   - Navigate to the first app, go to :code:`DEPLOYMENT` tab, and edit the :code:`captain-definition` path to :code:`./captain-definition-webserver`.

   - Then do the same for the second instance with :code:`./captain-definition-celery`

3. Caprover should now be able to deploy the app to its dedicated instance using the correct :code:`captain-definition` file, Dockerfile, and entry point (do this twice, once for the webserver and once for celery): ::

    caprover deploy

4. Additionaly, deploy a :code:`PostgreSQL` instance and a :code:`RabbitMQ` instance on the server using `Caprover One-Click Apps <https://caprover.com/docs/one-click-apps.html>`_.

5. At this stage, if not already the case, you must create a server app on a Fitbit dev account.
   Then retrieve the OAuth2 token and Fitbit credentials.

6. On the server, for the webserver and celery apps, fill in one environment variable per parameter :code:`env.str("ENV_VARIABLE")` in the setting files: :code:`SQS_HBS/settings.py` and :code:`SQS_HBS/settings_caprover.py`.

7. Finally, once the apps up and running, use the Django admin site to create users in the database as needed.

8. The rest should be automatic as Fitbit sends a :code:`POST` request to inform our server that new user data is available, which run celery tasks to retrieve and store it in the database.


For development
~~~~~~~~~~~~~~~

I recommend using Docker to easily and quickly set up a functional development environment, but the project can also be run natively.

**Using Docker**

1. Clone the project locally: ::

    git clone https://github.com/Ziip-dev/SQS_HBS.git

2. Ensure you have running :code:`PostgreSQL` and :code:`RabbitMQ` containers.

3. Create en :code:`.env` file with the parameters that are not hardcoded in the setting files: :code:`SQS_HBS/settings.py` and :code:`SQS_HBS/settings_dev.py`.

4. Run the helper script to automatically build the image and execute the container: ::

    ./start_container.sh


**Natively**

1. Clone the project locally: ::

    git clone https://github.com/Ziip-dev/SQS_HBS.git

2. Install dependencies: ::

    cd SQS_HBS/
    poetry install

3. Ensure you have running :code:`PostgreSQL` and :code:`RabbitMQ` containers.

4. Create a :code:`.env` file with the parameters that are not hardcoded in the setting files: :code:`SQS_HBS/settings.py` and :code:`SQS_HBS/settings_dev.py`.

5. Run the helper scripts to automatically start the webserver: ::

    ./run-webserver.sh
    ./run-celery.sh


Software stack
==============

This web app is configured as a PWA so it can be installed on mobile phones, which was the aim of the experiment.
It is built around:

- **Django** :: to leverage built-in user authentication and built-in class-based generic views.

- **django-fitbit** (see `Ziip-dev/django-fitbit <https://github.com/Ziip-dev/django-fitbit>`_) :: a django app that I have updated to manage Fitbit authentication, API requests, and database writes.

- **whitenoise** :: for static assets management.

- **Bulma** :: (via *django-simple-bulma*) to speed up the frontend development with ready-to-use components that can be easily combined to build a responsive interface.

- **PostgreSQL** :: for time series data management, which require simultaneous reads and writes for multiple users.

- **RabbitMQ** :: for job queuing, e.g. pending Fitbit Web API requests, database read/write, etc.

- **Celery** :: concurrent task execution, e.g. to simultaneously retrieve multiple users data from the Fitbit Web API.

- **eventlet** :: concurrent networking library to efficiently spawn hundreds of green thread (particularly adapted to async HTTP requests).


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
