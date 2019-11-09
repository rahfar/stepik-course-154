#!/bin/bash -x
#sudo /etc/init.d/mysql start
mysql -u root -p -e "CREATE DATABASE mydb CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -u root -p -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'Ab123456';"
mysql -u root -p -e "GRANT ALL ON mydb.* TO 'box'@'localhost';"