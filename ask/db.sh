sudo /etc/init.d/mysql restart
mysql -uroot -e "create database myproject;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'box'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
