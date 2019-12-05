FROM ubuntu

RUN apt-get update 
RUN apt -y install apache2 

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/www/html
ENV APACHE_LOG_DIR /var/log/apache2

COPY html /var/www/html
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY entrypoint.sh /entrypoint.sh

EXPOSE 80
ENTRYPOINT "/entrypoint.sh"
