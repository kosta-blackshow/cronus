FROM python:3.8.6-slim-buster

RUN useradd cronus

WORKDIR /home/cronus

COPY requirements.txt requirements.txt
COPY backend backend
COPY migrations migrations

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
RUN chmod a+x wait-for-postgres.sh

ENV FLASK_APP backend/cronus.py

RUN chown -R cronus:cronus ./
USER cronus

EXPOSE 5000
ENTRYPOINT ["./wait-for-postgres.sh"]