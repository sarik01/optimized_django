FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim
#RUN apk add postgresql-client build-base postgresql-dev

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service


# Perebroska portov chtobi bil dostup iz osnovnoy operac sistemi
#EXPOSE 8000





RUN pip install -r /temp/requirements.txt


# sozdat uzera bez parola
RUN adduser --disabled-password service-user

RUN chown -R service-user:service-user /service && chmod 755 /service

# polzovatel pod kotorim vse commandi konteynera budut zapuskatsa
USER service-user


CMD ["gunicorn","-b","0.0.0.0:8001","service.wsgi:application"]
