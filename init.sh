sudo rm /etc/nginx/sites-enabled/default
sudo cp /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/ && sudo mv nginx.conf default
sudo /etc/init.d/nginx restart