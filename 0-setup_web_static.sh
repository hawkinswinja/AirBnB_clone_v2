#!/usr/bin/env bash
#install nginx and update configuration
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Updates successful" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
hbnb="location \/hbnb_static {\n\talias \/data\/web_static\/current\/;\n}\nserver_name _;"
sed -i "s/server_name _;/$hbnb/g" /etc/nginx/sites-enabled/default
service nginx restart
