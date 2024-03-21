FROM ubuntu
RUN apt-get update
RUN apt-get install -y nginx
COPY nginx.conf /etc/nginx/sites-available/fundoo
#COPY start.sh /usr/local/bin/start.sh
#RUN chmod +x /usr/local/bin/start.sh
RUN ln -s /etc/nginx/sites-available/fundoo /etc/nginx/sites-enabled
RUN rm -rf /etc/nginx/sites-enabled/default
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
#CMD ["/usr/local/bin/start.sh"]
