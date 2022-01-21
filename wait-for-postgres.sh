#!/bin/bash

#set -e
#
#host="$1"
#shift
#
#until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "postgres" -c '\q'; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 1
#done
#
#>&2 echo "Postgres is up - executing command"

source venv/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - backend:server