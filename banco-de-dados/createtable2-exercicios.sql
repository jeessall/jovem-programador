CREATE TABLE LocaisDeApresentacao(
local_id INT PRIMARY KEY AUTO_INCREMENT,
nome_local VARCHAR(255) NOT NULL,
endereco VARCHAR(255),
capacidade INT
);

INSERT INTO LocaisDeApresentacao(nome_local, endereco, capacidade) VALUES
('Teatro Municipal', 'Rua das artes, 100', 1200),
('Auditório Central', 'Avenida da Cultura, 50', 800),
('Espaço Alternativo', 'Travessa da Criação, 10', 300);

CREATE TABLE EventosCulturais(
id_evento INT PRIMARY KEY AUTO_INCREMENT,
titulo_evento VARCHAR(255) NOT NULL,
tipo_evento VARCHAR(100),
data_evento DATE,
local_id INT, FOREIGN KEY (local_id) REFERENCES LocaisDeApresentacao(local_id)
);

INSERT INTO EventosCulturais(titulo_evento, tipo_evento, data_evento, local_id) VALUES
('Concerto da orquestra sinfônica', 'Concerto', '2025-07-15', 1),
('Peça: Sonho de uma noite de verão', 'Peça Teatral', '2025-08-01', 1),
('Exposição de arte moderna', 'Exposição', '2025-07-20', 3),
('Palestra sobre IA e futuro', 'Palestra', '2025-09-10', 2);

SELECT EC.titulo_evento, EC.tipo_evento, LA.nome_local
FROM EventosCulturais AS EC
JOIN LocaisDeApresentacao AS LA
ON EC.local_id = LA.local_id;

SELECT EC.titulo_evento, EC.data_evento, LA.nome_local
FROM EventosCulturais AS EC
JOIN LocaisDeApresentacao AS LA
ON EC.local_id = LA.local_id
WHERE EC.local_id = 1;

SELECT LA.nome_local, COUNT(EC.local_id) AS total_eventos
FROM LocaisDeApresentacao AS LA
LEFT JOIN EventosCulturais AS EC
ON LA.local_id = EC.local_id
GROUP BY LA.nome_local;

UPDATE LocaisDeApresentacao
SET capacidade = 400
WHERE local_id = 3;

SELECT titulo_evento, data_evento FROM EventosCulturais
WHERE data_evento BETWEEN '2025-07-01' AND '2025-07-31';

DELETE FROM EventosCulturais
WHERE id_evento = 4;

SELECT LA.nome_local FROM LocaisDeApresentacao AS LA
LEFT JOIN EventosCulturais AS EC ON LA.local_id = EC.local_id
WHERE EC.local_id IS NULL;

CREATE TABLE ingressos(
id_ingresso INT PRIMARY KEY AUTO_INCREMENT,
id_evento INT,
preco DECIMAL(10, 2),
tipo_ingresso VARCHAR(50),
data_venda DATE,
FOREIGN KEY (id_evento) REFERENCES EventosCulturais(id_evento)
);

INSERT INTO Ingressos(id_evento, preco, tipo_ingresso, data_venda) VALUES
(1, 80.00, 'Inteira', '2025-06-01'),
(1, 40.00, "Meia", '2025-06-05'),
(3, 60.00, 'Inteira', '2025-06-10');

SELECT EC.tipo_evento, I.tipo_ingresso, COUNT(*) AS quantidade_vendida, SUM(I.preco) AS total_arrecadado
FROM EventosCulturais AS EC
JOIN Ingressos AS I ON EC.id_evento = I.id_evento
GROUP BY EC.tipo_evento, I.tipo_ingresso
UNION ALL
SELECT 'TOTAL' AS tipo_evento, '—' AS tipo_ingresso, COUNT(*) AS quantidade_vendida, SUM(preco) AS total_arrecadado
FROM Ingressos;

SELECT tipo_ingresso, AVG(preco) AS preco_medio
FROM Ingressos
GROUP BY tipo_ingresso;

SELECT * FROM LocaisDeApresentacao;
SELECT * FROM EventosCulturais;
SELECT * FROM Ingressos;