FROM nginx:latest

# Копирование html файлов в -> /usr/share/nginx/html
# Копирование конфигов nginx

COPY html/ /usr/share/nginx/html
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf