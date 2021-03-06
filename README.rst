======================================================
Self-Quantification System for Health Behavior Support
======================================================

This is an experimental project for my PhD work aiming at providing users
with personalized recommendations to increase their physical activity level.

FEATURES
========

TODO/doc #2 - features


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

TODO/doc #3 - usage


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


ROADMAP
=======

- [ ] Check X-Fitbit-Signature --> peut-??tre d??j?? int??gr?? dans fitapp
    https://dev.fitbit.com/build/reference/web-api/developer-guide/best-practices/#Subscriber-Security

- [ ] Mettre en place le dashboard utilisateur (check templates).

- [ ] Int??grer l'analyse des donn??es d'activit?? physique de l'utilisateur.

- [ ] Int??grer la logique d'accompagnement en fonction de l'AP.

- [ ] Transformer en PWA (tout est dans les ressources collect??es + livre).

- [ ] Test IRL sur t??l??phone.



CHANGELOG
=========

- Int??grer Celery pour b??n??ficier des tasks asynchrones d??j?? ??crites dans
  fitapp, changer le database backend pour g??rer efficacement la concurrence
  et passer sur un execution pool bas?? sur des green threads.


- Basculer sur un syst??me de suivi par issues + pull request,
  le README va devenir plus gros que le code sinon...


- Solutionner le probl??me lors de requ??tes provenant d'utilisateurs
    diff??rents

    - d??claration d'une Server App sur mon compte fitbit.

    - tester si je r??cup??re les donn??es non-intraday pour Ines ET Anais.


- Faire fonctionner fitapp maintenant qu'elle est ?? jour et correctement
  d??clar??e.

  - mettre en place l'authentification des utilisateurs pour acc??der
    aux views fitbit.

      - livereload server for fast development of templates
        --> cancelled, trop de bugs lors des livereloads.

      - WhiteNoise setup for static files serving.



DEBUG NOTES
===========

CLI
---

- manually refresh tokens: `./manage.py refresh_tokens -v 3`
- manually refresh even non-expired tokens: `./manage.py refresh_tokens --all`
- del users with invalid refresh tokens: `./manage.py refresh_tokens --deauth`
  --> deauth removes UserFitbit
