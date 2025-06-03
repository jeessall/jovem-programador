CREATE TABLE clientes(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE
);
INSERT INTO clientes(nome, email) VALUES
('Maria Silva', 'maria@email.com'),
('João Moraes', 'joao@email.com');
UPDATE clientes
SET email = 'maria.silva@email.com'
WHERE id = 1;
DELETE FROM clientes
WHERE id = 1;
SELECT * FROM clientes;
SELECT nome FROM clientes;