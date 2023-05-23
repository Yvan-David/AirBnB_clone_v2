#!/usr/bin/env bash
# This script installs nginx on the computer it's run on.
#  It prints 'Hello world' when curled
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo chown -R "$USER:$USER" /var/www/html
echo 'Hello World!' > /var/www/html/index.html
sudo service nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
echo 'Hello Horlbeton' > /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
content="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
             try_files $uri $uri/ =404;
        }
        location /hbnb_static/ {
            alias /data/web_static/current/;
        }"
sudo rm -f /etc/nginx/sites-available/default
echo "$content" | sudo tee -a /etc/nginx/sites-available/default > /dev/null

sudo -sfn /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
