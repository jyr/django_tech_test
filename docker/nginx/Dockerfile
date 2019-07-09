FROM nginx:1.15.5-alpine

RUN apk update \
    && apk add curl \
    && apk add vim

COPY uwsgi_nginx.conf /etc/nginx/conf.d/default.conf
