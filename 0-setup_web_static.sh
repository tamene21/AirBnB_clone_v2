#!/usr/bin/env bash
# Prepare Web Server
apt-get update -y
# install nginx if not install
apt-get install nginx -y
# create a folder
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
# creating an html file
echo '<html>
 <head>
 </head>
 <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
# creating a link
ln -sf /data/web_static/releases/test/ /data/web_static/current
#give ownership of the daa
chown -hR ubuntu:ubuntu /data/

loc="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"

sudo sed -i "38i $loc" /etc/nginx/sites-available/default
service nginx restart
exit 0
