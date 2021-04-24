#!/bin/bash

docker rm *

docker-compose down

docker rm -f $(docker ps -a -q)

docker volume rm $(docker volume ls -q)

docker-compose rm django_hospital redis

docker-compose build --no-cache

docker-compose up