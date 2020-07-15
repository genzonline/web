sudo ln -sf /home/anar/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd ask
gunicorn -c /home/anar/box/web/etc/gunicorn-django.conf.py ask.wsgi
# gunicorn -c /home/anar/box/web/etc/gunicorn.conf.py hello:wsgi_application