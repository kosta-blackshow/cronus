FROM python:3.8.6-slim-buster

RUN useradd cronus

WORKDIR /home/cronus

COPY requirements.txt requirements.txt
COPY backend backend
COPY migrations migrations

RUN pip install -r requirements.txt
RUN pip install gunicorn

ENV FLASK_APP backend/cronus.py

RUN chown -R cronus:cronus ./
USER cronus

EXPOSE 5000
CMD ["flask", "run"]