sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "create database myproject;"
sudo mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'box'@'localhost';"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"
