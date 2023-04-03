#!/bin/sh

set -e

cd /backend/
. /opt/venv/bin/activate

echo "[entrypoint.sh] Collect static"
python manage.py collectstatic --noinput

echo "[entrypoint.sh] Apply migrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "[entrypoint.sh] Creates superuser"
python manage.py createsuperuser --noinput || true

echo "[entrypoint.sh] Start the server"
gunicorn src.wsgi:application --bind 0.0.0.0:8000
