#!/bin/sh
# wait-for-postgres.sh

set -e

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

. venv/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - backend:server