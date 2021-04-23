FROM python:3.8

WORKDIR /usr/src/app/

RUN apt update && apt install redis-server -y

RUN git clone https://github.com/zavyalovdv/django_hospital.git
RUN cd /usr/src/app/django_hospital/
# COPY . .

RUN chmod +x /usr/src/app/django_hospital/entrypoint.sh

RUN pip3 install -r requirements.txt

ENTRYPOINT ["entrypoint.sh"]
