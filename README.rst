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
the required poetry dependencies file ``pyproject.toml`` ::

    cd SQS_HBS/
    ln -s pyproject-dev.toml pyproject.toml

Create a python virtual environment ::

    poetry env use /path/to/python3.10

Install dependencies ::

    poetry install


USAGE
=====

TODO/doc - usage


LICENSE
=======

Distributed under the terms of the _GNU-AGPL-v3: https://github.com/Ziip-dev/SQS_HBS/blob/main/LICENSE, Python bindings of Fitbit WebAPI is free and open source software.


ISSUES
======

If you encounter any problems, please _file-an-issue: https://github.com/Ziip-dev/SQS_HBS/issues along with a detailed description.


REMINDER
========

The ``poetry.lock`` file has been temporarily git ignored in order to
regenerate the dependencies correctly in case of an environment change.


TODO - INCOMING
===============

- [ ] tester la récupération effective des données et l'alimentation de la bdd.

- [ ] mettre en place le dashboard utilisateur (check templates).

- [ ] intégrer l'analyse des données d'activité physique de l'utilisateur.

- [ ] intégrer la logique d'accompagnement en fonction de l'AP.

- [ ] intégrer en PWA (tout est dans les ressources collectées + livre).

- [ ] test IRL sur téléphone.


CHANGELOG
=========

- Faire fonctionner fitapp maintenant qu'elle est à jour et correctement
  déclarée.

      - mettre en place l'authentification des utilisateurs pour accéder
            aux views fitbit.

          - livereload server for fast development of templates.
          - WhiteNoise setup for static files serving.


DEBUG NOTES
===========

Request URL:

https://www.fitbit.com/oauth2/authorize?
response_type=code      # authorization code flow
&client_id=23BJPC
&redirect_uri=http%3A%2F%2F127.0.0.1%3A7000%2Ffitbit%2Fcomplete%2F
&scope=activity+nutrition+heartrate+location+nutrition+profile+settings+sleep+social+weight
&state=vRGYNCcCpJz3XIKEfKYsILUYaHcd4W

