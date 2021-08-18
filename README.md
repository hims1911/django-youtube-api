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
```
PS : jst ping me for that.

My Twitter handle - H1mSR0cK / https://twitter.com/H1mSR0cK



## Docker way:

First let just build the container 

```
sudo docker-compose build -d 
```

then 

```
sudo docker-compose up
```

Open the logs associated with the celery service: 

```
docker-compose logs -f 'celery'
```

Access the application via,

localhost:88888/

