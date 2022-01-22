FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /recipe_api

COPY requirements.txt requirements.txt

# postgres setup
RUN apk add --update --no-cache postgresql-client
# temp add-ons
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev

RUN pip install -r requirements.txt

# delete temp add-ons
RUN apk del .tmp-build-deps

# add user to switch from default user i.e. root, so that no one has root access
RUN adduser -D user
USER user

