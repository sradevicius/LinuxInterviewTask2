# Interview exercise -- API challenge

## About

This script can be used on it's own or it can be used in docker container. Repo contains dockerfile, so you can create image yourself with docker build
Docker image has also been [uploaded to dockerhub](https://hub.docker.com/r/sradevicius/linux_interview_test2)

## Usage
Both script and container expects 'username', 'token', 'email', 'reciever_email', and 'email_password'  environment variables to be passed on. In case of docker image I recomment to use -e flags to pass them on
For example:
> docker  run -e username='sradevicius' -e token='superSecretToken' -e email='sradeviciustestmail@gmail.com' -e email_password='SuperSecret' -e receiver_email='sradeviciustestmail@gmail.com' sradevicius/linux_interview_test2


## Issues/Problems/Limitations
I used simple SMTP login function to connect to my test gmail account, and it used password passed as environment variabled to script.
This is not a very good idea, as from security point of view I should look into implementing someking of Oauth authorization mechanism
<br>
Also this script picks up new pushed to git as commits but does not pick up cration of new repo as commit. 

## ToDo
Create somekind of Oauth log in for email
