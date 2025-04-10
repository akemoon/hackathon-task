FROM nginx:latest

COPY html/ /usr/share/nginx/html
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY log-daemon/nginx-log-daemon.sh /usr/local/bin/nginx-log-daemon.sh
RUN chmod +x /usr/local/bin/nginx-log-daemon.sh

RUN apt-get update && apt-get install -y coreutils procps supervisor

COPY log-daemon/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]