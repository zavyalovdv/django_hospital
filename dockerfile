FROM python:3

MAINTAINER @ZVPROJECT "daniilzavialov@yandex.ru"

WORKDIR /home/$USER/

RUN apt update && apt install redis-server git -y

# RUN chown -R ubuntu:ubuntu /usr/src/app/

RUN git clone https://github.com/zavyalovdv/django_hospital.git
RUN cd django_hospital/

# RUN chown -R $USER /usr/src/app/*

RUN chmod +x entrypoint.sh


# RUN echo pwd

# COPY requirements.txt .
# COPY entrypoint.sh .

RUN pip3 install -r requirements.txt

# COPY . .

# ENV django_hospital_secret_key="$django_hospital_secret_key"
# ENV db_password="$db_password"
# ENV db_username="$db_username"

ENTRYPOINT [ "entrypoint.sh" ]
