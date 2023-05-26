FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service
# Perebroska portov chtobi bil dostup iz osnovnoy operac sistemi
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt


# sozdat uzera bez parola
RUN adduser --disabled-password service-user

# polzovatel pod kotorim vse commandi konteynera budut zapuskatsa
USER service-user