#!/bin/bash

sleep 3

certbot --nginx -d puperpearl.ddns.net --email your@email.com --agree-tos --non-interactive

nginx -s reload