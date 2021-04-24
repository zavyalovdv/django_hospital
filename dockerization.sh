#!/bin/bash

docker-compose down

docker-compose rm redis django_hospital

docker-compose build --no-cache

docker-compose up