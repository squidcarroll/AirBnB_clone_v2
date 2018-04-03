#!/usr/bin/env bash
# script that sets everything up

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i "38i location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
