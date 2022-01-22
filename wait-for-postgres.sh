#!/bin/sh
# wait-for-postgres.sh

#set -e

#until pg_isready --username=postgres --host=postgres; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 1
#done
#
#>&2 echo "Postgres is up - executing command"
#psql --username=postgres --host=postgres --list

. venv/bin/activate
flask db upgrade
flask run
#exec gunicorn -b :5000 --access-logfile - --error-logfile - backend:server