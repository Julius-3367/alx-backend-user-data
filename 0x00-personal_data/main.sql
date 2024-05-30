-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON my_db.* TO 'root'@'localhost';

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    name VARCHAR(256),
    email VARCHAR(256),
    phone VARCHAR(16),
    ssn VARCHAR(16),
    password VARCHAR(256),
    ip VARCHAR(64),
    last_login TIMESTAMP,
    user_agent VARCHAR(512)
);

INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES 
("John Doe", "johndoe@example.com", "1234567890", "000-11-2222", "supersecret", "192.168.0.1", NOW(), "Mozilla/5.0");
INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES 
("Korir Julius", "korirjulius001@gmail.com", "0987654321", "111-22-3333", "root", "192.168.0.2", NOW(), "Mozilla/5.0");

