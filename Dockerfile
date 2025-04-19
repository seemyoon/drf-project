FROM python:3.12-alpine

MAINTAINER Oleksandr

ENV PYTHONDONTWRITEBYTECODE=1 \
    # ENV - Each environment variable affects the settings for Python, pip, Poetry, or the system to work more stable and automated.
    # PYTHONDONTWRITEBYTECODE=1 Disables creation of .pyc files to avoid writing them to disk (saves space)
    PYTHONUNBUFFERED=1 \
    # Disables Python output buffering (the output will be visible immediately, useful for logging)
    PIP_NO_CACHE_DIR=off \
    # Disables using cache when installing packages via pip (clean install)
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # Disables pip version checking (speeds up installations)
    PIP_DEFAULT_TIMEOUT=100 \
    # Sets a timeout for pip (100 seconds) when installing packages
    POETRY_VERSION=1.8.2 \
    # Installs a specific version of Poetry (a tool for managing dependencies in Python)
    POETRY_NO_INTERACTION=1 \
    # Disables Poetry's interactive mode (does not require user input)
    DEBIAN_FRONTEND=noninteractive \
    # Sets up package installation on Debian/Ubuntu without interactive prompts
    COLUMNS=80
    # Sets the terminal width to 80 characters (to display output correctly)

RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-dev curl
# --no-cache - does not cache downloaded packages to reduce the image size without leaving unnecessary files after installation.
# gcc — C compiler. Some Python packages or libraries may contain parts of code written in C or other languages. To install them, you need to compile these parts.
# musl-dev - to compile, you need to install libraries for working with musl.
# mariadb-dev - MariaDB in this context is simply used as a connector for working with MySQL. It is used as a more advanced alternative, providing additional features and improvements.
# curl is a tool for sending HTTP requests. It is often used to download files from the Internet or check the availability of services via API.
# curl example: during the process of setting up or deploying an application, you may need to download some additional files or make a request to the server.

RUN mkdir /app
WORKDIR /app
# WORKDIR /app as working directory

ENV POETRY_HOME=/usr/local/poetry
# POETRY_HOME is an additional environment variable for Poetry to work correctly, and such an environment variable helps the system know where to find Poetry and its files.
RUN curl -sSL https://install.python-poetry.org | python3 -
# installing poetry (from official doc for installation on Linux)
ENV PATH=$POETRY_HOME/bin:$PATH
# This step adds the path to the Poetry executables to the system PATH environment variable so that the system can find and run Poetry.
# $POETRY_HOME/bin:$PATH you add the new path to the beginning of the current PATH to give Poetry priority (if you want Poetry to run first).

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false
# Sets a setting for Poetry so that it does not create virtual environments when installing dependencies, and just worked with poetry
RUN poetry lock
# create lock file
RUN poetry install
# copy all from pyproject.toml and install