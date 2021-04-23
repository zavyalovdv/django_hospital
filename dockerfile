FROM python:3

WORKDIR /usr/src/app/django_hospital/

COPY requirements.txt .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN pip3 install -r requirements.txt

RUN apt update && apt install redis-server -y

#COPY . .
RUN git clone https://github.com/zavyalovdv/django_hospital.git

ENV django_hospital_secret_key="$django_hospital_secret_key"
ENV db_password="${db_password}"
ENV db_username="${db_username}"

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
