FROM python:2.7
MAINTAINER Salama AB <aksalj@aksalj.me>

ENV PYTHONUNBUFFERED 1
ENV APP_DIR /usr/src/app

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

ADD requirements.txt ${APP_DIR}
RUN pip install -r requirements.txt
COPY . ${APP_DIR}

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
