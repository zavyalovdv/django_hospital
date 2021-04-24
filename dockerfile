FROM python:3.8-buster

RUN git clone https://github.com/zavyalovdv/django_hospital.git

WORKDIR django_hospital/

RUN chmod +x entrypoint.sh

RUN pip3 install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
