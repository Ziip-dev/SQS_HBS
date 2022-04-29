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

- [ ] solutionner le problème lors de requêtes provenant d'utilisateurs
    différents
    - [ ] test Anais sur l'endpoint intraday voir ce que je récupère.
    - [ ] déclaration d'une Server App sur mon compte fitbit.
    - [ ] tester si je récupère les données non-intraday pour Ines ET Anais.

- [ ] fitbit intraday data request form!
    - possible with client or server application.
    - refresh token only supported with Authorization Code Grant flow.

- [ ] solutionner l'alimentation de la bdd.

    - requête testée sur:
      http://127.0.0.1:7000/fitbit/get_data/activities/minutesSedentary/?base_date=2022-04-01&period=1d
      OK


- [ ] mettre en place le dashboard utilisateur (check templates).

- [ ] intégrer l'analyse des données d'activité physique de l'utilisateur.

- [ ] intégrer la logique d'accompagnement en fonction de l'AP.

- [ ] transformer en PWA (tout est dans les ressources collectées + livre).

- [ ] test IRL sur téléphone.


CHANGELOG
=========

- Faire fonctionner fitapp maintenant qu'elle est à jour et correctement
  déclarée.

  - mettre en place l'authentification des utilisateurs pour accéder
    aux views fitbit.

    - livereload server for fast development of templates
       -> cancelled, trop de bugs lors des livereloads.

    - WhiteNoise setup for static files serving.


DEBUG NOTES
===========

Anais
-----

- la commande `./manage.py refresh_tokens --all` renouvelle bien le token
  d'authentification non-expiré.

- encodedId:  7D8L5Z

- expires_at: 1650579868.82373

