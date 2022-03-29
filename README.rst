======================================================
Self-Quantification System for Health Behavior Support
======================================================

This is an experimental project for my PhD work aiming at providing users
with personalized recommendations to increase their physical activity level.

Installation
============

Prerequisites
-------------

- git
- python 3 (tested with 3.10)
- poetry (optional but recommended)


For production (temp instructions)
----------------------------------

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



REMINDER
========

The ``poetry.lock`` file has been temporarily git ignored in order to
regenerate the dependencies correctly in case of an environment change.


- [ ] faire fonctionner fitapp maintenant qu'elle est à jour et
     correctement déclarée
