FROM python:3

WORKDIR /usr/src/app

RUN apt update && apt upgrade -y && apt install redis-server -y

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
