# django-youtube-api


This repository contains the Application that allows user to fetch the data via youtube public api.

Steps required before running the application:

1) We have to setup the youtube public api account, from there will get the youtube API_KEY

2) We should have Python3 installed system or Docker is more than enough to build the application.


Let's clone the repo first.

You have to add the Secret key for the django application create the .env file and setup the values as
```
SECRET_KEY= XYZ
DEBUG=TRUE
API_KEY=KEY1,KEY2,...
```
PS : jst ping me for that.

My Twitter handle - H1mSR0cK / https://twitter.com/H1mSR0cK



## Docker way:

First let just build the container 
```
sudo docker-compose build
```

```
sudo docker-compose up -d
```

to get the running containers
```
sudo docker ps
```

get the container ID and then

```
sudo docker inspect ID
```


It will give the IP address 

Queries:

to get the videos list : 
```IP:88888/api/videos```
<br>
to perform search:
```IP:8888/api/videos?title=valuex1description=value2```
