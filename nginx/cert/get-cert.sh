#!/bin/bash

sleep 3

certbot --nginx -d puperpearl.ddns.net --email a.kharitonovt.rex@gmail.com --agree-tos --non-interactive

nginx -s reload