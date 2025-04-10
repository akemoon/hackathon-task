FROM php:8.2-apache

COPY ./info.php /var/www/html/

# Specify / page and activate it
RUN echo "DirectoryIndex info.php" > /etc/apache2/conf-available/index.conf \
    && a2enconf index

EXPOSE 80