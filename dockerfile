FROM python:3.8

WORKDIR /usr/src/app/

RUN apt update && apt install redis-server git python3-pip python3-venv bash -y

# RUN chown -R ubuntu:ubuntu /usr/src/app/

RUN python3 -m venv venv

RUN bash source venv/bin/activate

RUN git clone https://github.com/zavyalovdv/django_hospital.git
WORKDIR /usr/src/app/django_hospital/

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

ENTRYPOINT [ entrypoint.sh ]
