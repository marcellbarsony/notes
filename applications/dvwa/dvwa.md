# Damn Vulnerable Web App (DVWA)

Ensure Network Adapter is set to **NAT**

## Setup

Clone the [repository](https://github.com/digininja/DVWA)
```sh
cd /var/www/html
sudo git clone https://github.com/digininja/DVWA.git
```

Start Apache2
```sh
sudo service apache2 start
```

## Configuration

### Config File

Create a [config file](https://github.com/digininja/DVWA#configurations)
```sh
cd DVWA/config
sudo cp config.inc.php.dist config.inc.php
```

[Database Setup](https://github.com/digininja/DVWA#database-setup)
```sh
sudo service mariadb start
```

### Database Setup

Become root
```sh
sudo su
```

Configure new database user
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
