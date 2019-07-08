FROM python:3.7-alpine

RUN apk update \
    && apk add --no-cache --virtual bash \
    && apk add gcc \
    && apk add musl-dev \
    && apk add linux-headers \
    && apk add jpeg-dev \
    && apk add zlib-dev \
    && apk add libffi-dev \
    && apk add curl \
    && apk add vim

# install pypi packages
COPY requirements.txt /requirements.txt
#COPY app/urbvan/requirements/base.txt /home/docker/code/urbvan/requirements/base.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /var/www/html/

USER 1000:1000

#CMD ["uwsgi", "--ini", "/uwsgi.ini"]
CMD ["uwsgi", "--http", ":8000", "--chdir", "/var/www/html/", "--module", "urbvan.wsgi"]
