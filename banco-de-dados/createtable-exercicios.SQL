CREATE TABLE produtos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
preco DECIMAL(10, 2) NOT NULL,
estoque INT DEFAULT 0
);
ALTER TABLE produtos
ADD texto VARCHAR(50);
INSERT INTO produtos(nome, preco, estoque) VALUES
('Caderno', 12.50 , 100);
UPDATE produtos
SET preco = 15.00
WHERE id = 1;
UPDATE produtos
SET estoque = estoque - 10
WHERE id = 1;
DELETE FROM produtos
WHERE id = 1;
SELECT * FROM produtos 
WHERE estoque > 50;
SELECT nome, preco FROM produtos
WHERE preco < 20;
SELECT * FROM produtos
WHERE nome LIKE 'M%';
SELECT COUNT(*) FROM produtos;
SELECT MAX(preco) FROM produtos;
SELECT AVG(preco) FROM produtos;
SELECT * FROM produtos
ORDER BY preco DESC;
SELECT * FROM produtos
ORDER BY preco ASC
LIMIT 3;
SELECT * FROM produtos
WHERE preco LIKE '%12.50';
 BEGIN;
INSERT INTO produtos(nome, preco, estoque)
VALUES('Caneta', 3.00, 200);
ROLLBACK;
 BEGIN;
INSERT INTO produtos(nome, preco, estoque)
VALUES('Mochila', 37.00, 120);
INSERT INTO produtos(nome, preco, estoque)
VALUES('Borracha', 1.50, 150);
COMMIT;
 BEGIN;
INSERT INTO produtos(nome, preco, estoque)
VALUES ('Apontador', 2.50, 50);
SAVEPOINT ponto1;
INSERT INTO produtos(nome, preco, estoque)
VALUES ('Marcador', 4.00, 70);
ROLLBACK TO ponto1;
COMMIT;
SELECT * FROM produtos;