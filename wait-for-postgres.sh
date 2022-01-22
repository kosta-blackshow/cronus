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
exec gunicorn -w 4 --access-logfile - --error-logfile - -b :5000 backend:server --timeout 300