FROM python:3.6-alpine

MAINTAINER Derek M. Frank <derek at frank dot sh>
WORKDIR /usr/src/app

# System dependencies.
RUN apk update && apk add \
    gcc \
    musl-dev

# Package dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Add application.
COPY . .

EXPOSE 5000
CMD ["gunicorn", \
     "-b", "0.0.0.0:5000", \
     "-w", "4", \
     "-k", "gevent", \
     "project:app"]
