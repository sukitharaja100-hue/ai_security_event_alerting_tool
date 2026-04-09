CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    ip VARCHAR(50),
    status VARCHAR(20),
    time DATETIME
);
