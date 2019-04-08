FROM python:3.7-stretch
LABEL author="Beauli Zhu"

RUN apt-get update && apt-get -y install logrotate

RUN pip install pipenv -i https://mirrors.aliyun.com/pypi/simple

ENV PYTHON_ENV=development

#Copy logrotate nginx configuration
COPY config/logrotate.d/gunicorn /etc/logrotate.d/

RUN service cron start

ADD . /code
WORKDIR /code

RUN mkdir -p /log/api/
RUN mkdir -p /log/web/

RUN pipenv install --system

EXPOSE 8000 8001

CMD ["bin/start_app_web.sh"]