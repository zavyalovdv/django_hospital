FROM python:3.8

WORKDIR /usr/src/app/

RUN apt update && apt install redis-server git -y

RUN git clone https://github.com/zavyalovdv/django_hospital.git
WORKDIR /usr/src/app/django_hospital/
# COPY . .

RUN chmod +x entrypoint.sh

RUN pip3 install -r requirements.txt

ENTRYPOINT ["entrypoint.sh"]
