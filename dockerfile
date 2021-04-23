FROM python:3

WORKDIR /usr/src/app/

RUN apt update && apt install redis-server git -y

# RUN git clone https://github.com/zavyalovdv/django_hospital.git
# RUN cd django_hospital/
# RUN echo pwd

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

COPY . .

# ENV django_hospital_secret_key="$django_hospital_secret_key"
# ENV db_password="$db_password"
# ENV db_username="$db_username"

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
