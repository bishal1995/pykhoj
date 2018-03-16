FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

RUN pip3 install --proxy=http://172.16.30.20:8080/ \
         pandas \
         numpy \
         matplotlib \
         seaborn \
         
                                