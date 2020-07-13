gunicorn --bind='0.0.0.0:8080' hello:wsgi_application
sudo ln -sf /home/anar/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart