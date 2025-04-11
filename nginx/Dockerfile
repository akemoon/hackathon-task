FROM nginx:latest

# Копируем HTML и конфиги nginx
COPY html/ /usr/share/nginx/html
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем лог-демон
COPY log-daemon/nginx-log-daemon.sh /usr/local/bin/nginx-log-daemon.sh
RUN chmod +x /usr/local/bin/nginx-log-daemon.sh

# Устанавливаем необходимые пакеты, включая certbot и nginx plugin
RUN apt-get update && \
    apt-get install -y coreutils procps supervisor \
                       certbot python3-certbot-nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Копируем конфиг supervisord
COPY log-daemon/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Старт через Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
