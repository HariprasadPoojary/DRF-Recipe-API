FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /recipe_api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# add user to switch from default user i.e. root, so that no one has root access
RUN adduser -D user
USER user

