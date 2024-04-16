#!/bin/sh -x
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear
cp -rf /app/static/. /backend_static/
gunicorn --bind 0.0.0.0:8000 config.wsgi
