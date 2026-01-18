CREATE DATABASE IF NOT EXISTS animal_db;
USE animal_db;

CREATE TABLE IF NOT EXISTS predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    filepath VARCHAR(255) NOT NULL,
    label VARCHAR(50) NOT NULL COMMENT 'Tên loài vật dự đoán',
    confidence FLOAT NOT NULL COMMENT 'Độ chính xác (0.0 - 1.0)',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO predictions (filename, filepath, label, confidence) 
VALUES ('test_init.jpg', 'uploads/test_init.jpg', 'Test System', 1.0);