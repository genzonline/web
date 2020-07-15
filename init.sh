sudo ln -sf /home/anar/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c /home/anar/box/web/etc/gunicorn.conf.py hello:wsgi_application