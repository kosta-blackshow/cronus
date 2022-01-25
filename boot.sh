#!/bin/sh
. venv/bin/activate
flask db upgrade
exec gunicorn -w 2 --access-logfile - --error-logfile - -b :5000 backend:server --timeout 300