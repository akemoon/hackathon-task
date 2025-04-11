FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    nginx \
    certbot \
    python3-certbot-nginx \
    supervisor \
    coreutils \
    procps \
    bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
    
COPY html/ /usr/share/nginx/html
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY log-daemon/nginx-log-daemon.sh /usr/local/bin/nginx-log-daemon.sh
COPY cert/get-cert.sh /usr/local/bin/get-cert.sh
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN chmod +x /usr/local/bin/*.sh

RUN adduser --system --no-create-home --disabled-login nginx

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]