# Configuration

## Config File

1. Create a [config file](https://github.com/digininja/DVWA#configurations)
```sh
cd DVWA/config
sudo cp config.inc.php.dist config.inc.php
```

2. [Database Setup](https://github.com/digininja/DVWA#database-setup)
```sh
sudo service mariadb start
```
## Database Setup

3. Become root
```sh
sudo su
```

4. Configure new database user
```sh
mysql

# Create database `dvwa`
mysql> create database dvwa;
Query OK, 1 row affected (0.00 sec)

# Create database user `dvwa`
mysql> create user dvwa@localhost identified by 'p@ssw0rd';
Query OK, 0 rows affected (0.01 sec)

# Grant all privileges to `dvwa`
mysql> grant all on dvwa.* to dvwa@localhost;
Query OK, 0 rows affected (0.01 sec)

# Reload privileges table
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
```
