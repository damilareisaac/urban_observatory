FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/app

# set working directory
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
