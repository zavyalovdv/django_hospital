FROM python:3.8

WORKDIR /usr/src/app/

RUN apt update && apt install redis-server git python3-pip python3-venv -y

# RUN git clone https://github.com/zavyalovdv/django_hospital.git
COPY . .
WORKDIR /usr/src/app/django_hospital/

RUN chmod +x entrypoint.sh

RUN pip3 install -r requirements.txt

ENTRYPOINT [ entrypoint.sh ]
