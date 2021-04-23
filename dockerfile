FROM python:3.8

WORKDIR /usr/src/app/

RUN apt update && apt install redis-server -y

RUN git clone https://github.com/zavyalovdv/django_hospital.git
# COPY . .

RUN chmod +x django_hospital/entrypoint.sh

RUN pip3 install -r django_hospital/requirements.txt

ENTRYPOINT ["django_hospital/entrypoint.sh"]
