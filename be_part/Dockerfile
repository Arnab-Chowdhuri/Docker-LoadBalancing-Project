FROM python:3.6

ENV CHATDB=chat_db
ENV CHATDBUSER=admin
ENV CHATDBPASSWORD=admin
#ENV CHATDBHOST=db_c

RUN apt-get update
RUN apt-get install --yes python3-pip

WORKDIR /project
COPY new_chatapp_docker .

WORKDIR /project/
RUN pip3 install mysqlclient
RUN pip3 install -r requirements.txt
#CMD ["/bin/bash", "-c", "pip3 install -r requirements.txt"]

EXPOSE 8000

WORKDIR /project/fundoo/
CMD ["/bin/bash", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
