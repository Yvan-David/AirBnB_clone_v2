#!/usr/bin/env bash
# This script installs nginx on the computer it's run on.
#  It prints 'Hello world' when curled
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo chown -R "$USER:$USER" /var/www/html
echo 'Hello World!' > /var/www/html/index.html
sudo service nginx start
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test
echo 'Hello Horlbeton' > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
content="server {
    location /current/hbnb_static {
        alias /data/web_static/current/;
    }
}"
echo "$content" > /etc/nginx/conf.d/testy.conf
sudo service nginx restart
