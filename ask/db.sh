sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "CREATE DATABASE stepic_web;"
sudo mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost';"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"
