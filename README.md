# Interview exercise -- API challenge

## Usage

This script can be used on it's own or it can be used in docker container. Repo contains dockerfile, so you can create image yourself with docker build
Both script and container expects 'username' and 'token' environment variables to be passed on. In case of docker image I recomment to use -e flags to pass them on
Docker image has also been [uploaded to dockerhub](https://hub.docker.com/r/sradevicius/linux_interview_test2)

## ToDo

I still haven't written code to send email once commit is detected.
