FROM ubuntu
RUN apt-get update
RUN apt-get install -y nginx
COPY config_file /etc/nginx/sites-available/config_file
RUN ln -s /etc/nginx/sites-available/config_file /etc/nginx/sites-enabled
RUN rm -rf /etc/nginx/sites-enabled/default
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
