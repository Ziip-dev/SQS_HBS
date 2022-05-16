======================================================
Self-Quantification System for Health Behavior Support
======================================================

This is an experimental project for my PhD work aiming at providing users
with personalized recommendations to increase their physical activity level.

FEATURES
========

TODO/doc - features


REQUIREMENTS
============

- git
- python 3 (tested with 3.10)
- poetry (optional but recommended)


INSTALLATION
============

For production (temporary)
--------------------------

Clone the project repository::

    git clone https://github.com/Ziip-dev/SQS_HBS.git

Create a soft link from the prod dependencies file ``pyproject-prod.toml`` to
the required poetry dependencies file ``pyproject.toml`` ::

    cd SQS_HBS/
    ln -s pyproject-prod.toml pyproject.toml

Create a python virtual environment ::

    poetry env use /path/to/python3.10

Install dependencies ::

    poetry install


For development
---------------

Clone both project repositories::

    git clone https://github.com/Ziip-dev/SQS_HBS.git
    git clone https://github.com/Ziip-dev/django-fitbit.git

Create a soft link from the dev dependencies file ``pyproject-dev.toml`` to
the required poetry dependencies file ``pyproject.toml``::

    cd SQS_HBS/
    ln -s pyproject-dev.toml pyproject.toml

Create a python virtual environment::

    poetry env use /path/to/python3.10

Install dependencies::

    poetry install


Deployment
----------

- dockerisation
- collectstatic to run on server


USAGE
=====

TODO/doc - usage


LICENSE
=======

Distributed under the terms of the `GNU AGPL v3`_.

.. _GNU AGPL v3: https://github.com/Ziip-dev/SQS_HBS/blob/main/LICENSE


ISSUES
======

If you encounter any problems, please `file an issue`_ along with a
detailed description.

.. _file an issue: https://github.com/Ziip-dev/SQS_HBS/issues


REMINDER
========

The current ``poetry.lock`` file corresponds to the ``pyproject-dev.toml``
file.

For deployment in production, remember to delete the lock file in order to
switch to the ``pyproject-prod.toml`` dependencies.


TODO - INCOMING
===============

--> il me faut les intraday, pas le choix pour faire du suivi journalier.
    Bien que la fonction préparant la requête existe dans fitapp.api,
    il faut modifier fitapp.utils.get_fitbit_data() pour pouvoir call
    fitapp.api.intraday_time_series() à l'instar de fitapp.api.time_series()
    vérifier dans les forks avant tout:

::

                            +-------------------------+
                            | fitapp.views.get_data() |
                            +-------------------------+
                                         |
                                         |
                                        \ /
                                         '
                         +--------------------------------+
                         | fitapp.utils.get_fitbit_data() |
                         +--------------------------------+
                                         |
                            _____________|______________
                           |                           |
                          \ /                         \ /
                           '                           '
         +--------------------------+         +-----------------------------------+
         | fitapp.api.time_series() |         | fitapp.api.intraday_time_series() |
         +--------------------------+         +-----------------------------------+


- [ ] Passer sur les données intraday :

    - [x] fitbit intraday data request form!
        - possible with client or server application.
        - refresh token only supported with Authorization Code Grant flow.

    - [ ] test Anais sur l'endpoint intraday --> méthode à modifier d'abord



- [ ] Changer sqlite ou définir config Celery pour fonctionnement concurrent
      "If using sqlite, create a celery configuration that prevents the fitapp
       celery tasks from being executed concurrently."
       Celery is required only for managing queued tasks for subscripiton??
       C'est à moi d'intégrer Celery dans ma webapp si je veux en gros...
       Pour l'instant on va écrire dans la base de données hein.



- [ ] Alimenter la BDD :

    - [x] requête manuelle OK:
      http://127.0.0.1:7000/fitbit/get_data/activities/minutesSedentary/?base_date=2022-04-01&period=1d

    - [x] requête générée automatiquement OK:
      <a href="{% url 'fitbit-data' category='activities' resource='minutesSedentary' %}?base_date=2022-04-01&period=1d"></a>

    - [x] pas la peine de variabiliser les paramètres des requêtes `base_date`
      et `period` car les requêtes seront gérées automatiquement et non par des
      liens.

    - [ ] vu que la view de `fitapp` permettant de récupérer les données est
          une vue AJAX, il faut que je la requête automatiquement sans
          intervention de l'utilisateur --> javascript bonjour !
          REMARQUE : pour automatiser les récupérations, soit je déclenche
          suite à la réception de la notif de subscription, soit je traite
          en JS (serviceworker etc.)



    - [ ] Subscription fitbit integration
        Permet de recevoir une requête POST de Fitbit sur un endpoint
        public pour être notifié qu'un utilisateur a de nouvelles données
        dispo.

        ATTENTION : https://dev.fitbit.com/build/reference/web-api/developer-guide/using-subscriptions/#Responding-to-a-Notification

        - [ ] Create a web service endpoint that can receive the HTTPS POST
              notifications described in Notifications. Make sure this endpoint
              is accessible from fitbit.com servers.

        - [x] Configure a subscriber to point to this endpoint as described in
              Configure a Subscriber.

        - [ ] Verify your subscriber endpoint as described in Verify a
              Subscriber. This will require adding code to respond correctly to
              a verification code.

        - [ ] Add subscriptions as described in Add a Subscription.




- [ ] Mettre en place le dashboard utilisateur (check templates).

- [ ] Intégrer l'analyse des données d'activité physique de l'utilisateur.

- [ ] Intégrer la logique d'accompagnement en fonction de l'AP.

- [ ] Transformer en PWA (tout est dans les ressources collectées + livre).

- [ ] Test IRL sur téléphone.



CHANGELOG
=========


- [x] solutionner le problème lors de requêtes provenant d'utilisateurs
    différents

    - [x] déclaration d'une Server App sur mon compte fitbit.

    - [x] tester si je récupère les données non-intraday pour Ines ET Anais.



- [x] Faire fonctionner fitapp maintenant qu'elle est à jour et correctement
  déclarée.

  - [x] mettre en place l'authentification des utilisateurs pour accéder
    aux views fitbit.

      - [x] livereload server for fast development of templates
        --> cancelled, trop de bugs lors des livereloads.

      - [x] WhiteNoise setup for static files serving.



DEBUG NOTES
===========

CLI
---

- manually refresh tokens: `./manage.py refresh_tokens -v 3`
- manually refresh even non-expired tokens: `./manage.py refresh_tokens --all`
- del users with invalid refresh tokens: `./manage.py refresh_tokens --deauth`
  --> deauth removes UserFitbit
