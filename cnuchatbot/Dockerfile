FROM python:3.9.7

ENV PYTHONBUFFERED 1

RUN apt-get -y update

RUN mkdir /srv/cnuchatbot

WORKDIR /srv/cnuchatbot

ADD ./ ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
