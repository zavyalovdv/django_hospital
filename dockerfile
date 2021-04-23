FROM python:3

MAINTAINER @ZVPROJECT "daniilzavialov@yandex.ru"

WORKDIR /usr/src/app/

RUN apt update && apt install redis-server git -y

# RUN chown -R ubuntu:ubuntu /usr/src/app/

RUN git clone https://github.com/zavyalovdv/django_hospital.git
# RUN cd django_hospital/
# RUN echo pwd

# COPY requirements.txt .
# COPY entrypoint.sh .

RUN pip3 install -r django_hospital/requirements.txt

RUN chmod +x django_hospital/entrypoint.sh

# COPY . .

# ENV django_hospital_secret_key="$django_hospital_secret_key"
# ENV db_password="$db_password"
# ENV db_username="$db_username"

ENTRYPOINT [ "entrypoint.sh" ]
