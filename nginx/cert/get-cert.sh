#!/bin/bash

sleep 3

certbot --nginx -d hello-world.zapto.org --email a.kharitonovt.rex@gmail.com --agree-tos --non-interactive

nginx -s reload