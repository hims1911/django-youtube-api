FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /fam_pay_test
WORKDIR /fam_pay_test
ADD . /fam_pay_test
CMD pwd
RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=fam_pay_test.settings
ADD . /m
EXPOSE 8888
