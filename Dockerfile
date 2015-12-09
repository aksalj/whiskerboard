FROM python:2.7
MAINTAINER Salama AB <aksalj@aksalj.me>

ENV PYTHONUNBUFFERED 1
ENV APP_DIR /usr/src/app
ENV DATA_DIR

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

ADD requirements.txt ${APP_DIR}
RUN pip install -r requirements.txt
ADD . ${APP_DIR}

#RUN python manage.py syncdb
#RUN python manage.py migrate

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
