###############################################
# Base Image
###############################################
FROM python:3.10-slim-bullseye as python-base
ARG user=ziip

# Environment variables
ENV APP_DIR=/home/${user}/app \
    \
    # Python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # prevents python from creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/home/${user}/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # Paths - where requirements + virtual env will live
    PYSETUP_PATH="/home/${user}/pysetup"
    # VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
# ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
ENV PATH="$POETRY_HOME/bin:$PATH"


###############################################
# Builder Image
###############################################
FROM python-base as builder-base

# Install OS-level dependencies (as root)
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get purge -y --autoremove \
    && apt-get autoclean \
    && apt-get install --no-install-recommends -y \
        # dep to install poetry
        curl \
        # dep to install django-fitbit app
        git \
    # cleaning up unused files to reduce image size
    && rm -rf /var/lib/apt/lists/*

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# Create directory for source code
WORKDIR $PYSETUP_PATH

# Copy project requirement files here to ensure they will be cached.
COPY pyproject.toml ./

# Install runtime deps (uses $POETRY_VIRTUALENVS_IN_PROJECT internally)
# RUN poetry install $(test "$YOUR_ENV" == production && echo "--no-dev")
RUN poetry install --no-dev


###############################################
# Production Image
###############################################
FROM python-base as production
# Retrieve only the environment set up at the last stage
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copy source code
WORKDIR $APP_DIR
COPY ./SQS_HBS ./SQS_HBS
COPY ./dashboard ./dashboard
COPY ./staticfiles ./staticfiles
COPY manage.py docker-entrypoint.sh ./

# Set execution permission and proper ownership
RUN chmod a+x docker-entrypoint.sh

# Create and switch to non-root user
ARG user=ziip
RUN useradd --system --user-group --shell /bin/bash ${user}

RUN chown -R ${user}:${user} /home/${user}/
USER ${user}

# Server
EXPOSE 7000
ENTRYPOINT ["./docker-entrypoint.sh"]
