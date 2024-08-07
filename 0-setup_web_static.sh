#!/usr/bin/env bash
# A Bash script that sets web servers for the deployment of 'web_static'

sudo apt-get -y update
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
#html file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton ia a cool School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
#symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
