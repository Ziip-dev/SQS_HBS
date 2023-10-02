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


Installation
------------


For production (temporary)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the project repository::

    git clone https://github.com/Ziip-dev/SQS_HBS.git

Create a python virtual environment ::

    poetry env use /path/to/python3.10

Install dependencies ::

    poetry install


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






The app is containerised for easier testing and deployment.
You can either run it in a Docker container, automatically deploy it using Caprover on a server, or run it natively:


Docker
------

1. Run the helper script to automatically build the image and execute the container:

   ::

       $ ./start_container.sh


Caprover PaaS
-------------

1. Use the Caprover CLI to deploy the Dockerfile on a server and automatically build it there (your remote server has to run Caprover):

   ::

       $ captain deploy


Software stack details
======================

This web app is configured as a PWA so it can be installed on mobile phones, which was the aim of the experiment.
It is built around:

- **Django** :: to leverage built-in user authentication and built-in class-based generic views.

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
