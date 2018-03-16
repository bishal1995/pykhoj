FROM ubuntu:latest
ENV http_proxy http://172.16.30.20:8080/
ENV https_proxy https://172.16.30.20:8080/
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
ADD . /home/
RUN ls /home
RUN pip3 --proxy=http://172.16.30.20:8080/ \
         --timeout 1000 \
         install \
	     -r \
         /home/requirements.txt\
