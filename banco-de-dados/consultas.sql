-- **********************************

-- **********************************

-- ** Estrutura definida para MySQL**

-- **********************************

-- **********************************

 

-- Criação da tabela cliente

CREATE TABLE cliente (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(110) NOT NULL,

    email VARCHAR(110) NOT NULL,

    telefone VARCHAR(20),

    data_nascimento DATE

);


INSERT INTO cliente (nome, email, telefone, data_nascimento) VALUES

('João Silva', 'joao.silva@example.com', '(11) 91234-5678', '1985-07-10'),

('Maria Oliveira', 'maria.oliveira@example.com', '(21) 99876-5432', '1990-02-15'),

('Carlos Souza', 'carlos.souza@example.com', '(31) 98765-4321', '1983-11-25'),

('Ana Pereira', 'ana.pereira@example.com', '(41) 91234-8765', '1978-05-30'),

('Fernanda Lima', 'fernanda.lima@example.com', '(51) 92345-6789', '1992-09-08'),

('Ricardo Martins', 'ricardo.martins@example.com', '(61) 91234-5678', '1987-03-12'),

('Camila Ferreira', 'camila.ferreira@example.com', '(71) 98765-1234', '1995-06-22'),

('Pedro Santos', 'pedro.santos@example.com', '(81) 99876-4321', '1980-10-30'),

('Patrícia Gomes', 'patricia.gomes@example.com', '(91) 91234-9988', '1988-12-05'),

('Juliana Costa', 'juliana.costa@example.com', '(95) 94567-8901', '1993-07-19'),

('João Almeida', 'joao.almeida@example.com', '(85) 97865-3214', '1984-08-15'),

('Renata Azevedo', 'renata.azevedo@example.com', '(31) 95432-1876', '1991-05-29'),

('Bruno Melo', 'bruno.melo@example.com', '(21) 96457-4321', '1989-04-17'),

('Luciana Duarte', 'luciana.duarte@example.com', '(41) 92134-6578', '1994-11-23'),

('Thiago Cardoso', 'thiago.cardoso@example.com', '(51) 93214-5678', '1986-01-14');



-- Criação da tabela produto

CREATE TABLE produto (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nome_produto VARCHAR(255) NOT NULL,

    descricao TEXT,

    preco DECIMAL(10, 2) NOT NULL

);


INSERT INTO produto(nome_produto, descricao, preco) VALUES

('Notebook Dell', 'Notebook de alta performance com 16GB RAM e 512GB SSD', 4500.00),

('Smartphone Samsung Galaxy', 'Smartphone Android com 128GB de armazenamento', 1200.00),

('Smart TV LG', 'Televisão 4K de 55 polegadas com HDR', 2800.00),

('Fone de Ouvido JBL', 'Fone de ouvido sem fio com cancelamento de ruído', 350.00),

('Impressora HP', 'Impressora multifuncional com Wi-Fi', 650.00),

('Tablet Apple iPad', 'Tablet com tela retina de 10.2 polegadas e 128GB', 3300.00),

('Monitor Samsung', 'Monitor curvo de 27 polegadas Full HD', 1200.00),

('Teclado Mecânico', 'Teclado mecânico RGB com switches azuis', 450.00),

('Mouse Gamer', 'Mouse óptico com 7 botões programáveis e DPI ajustável', 300.00),

('Câmera Canon DSLR', 'Câmera fotográfica com sensor APS-C e lente 18-55mm', 4200.00),

('Smartwatch Xiaomi', 'Relógio inteligente com monitoramento de atividades', 500.00),

('Caixa de Som Bluetooth', 'Caixa de som portátil com 20W de potência', 250.00),

('Carregador Portátil', 'Power bank de 10.000mAh com carregamento rápido', 49.99),

('Console PlayStation 5', 'Console de última geração com SSD ultrarrápido', 4900.00),

('Drone DJI Mini', 'Drone compacto com câmera 4K e GPS', 3600.00),

('HD Externo', 'Disco rígido portátil de 1TB USB 3.0', 300.00),

('Roteador Wi-Fi', 'Roteador com 4 antenas e suporte a 5GHz', 250.00),

('Webcam Logitech', 'Webcam Full HD com microfone embutido', 280.00),

('Ventilador de Mesa', 'Ventilador de 40cm com 3 velocidades', 149.99),

('Air Fryer', 'Fritadeira elétrica sem óleo com 3,5L de capacidade', 400.00),

('Geladeira Brastemp', 'Geladeira duplex frost free com 400L de capacidade', 3299.90),

('Fogão Consul', 'Fogão de 4 bocas com acendimento automático', 1200.00),

('Micro-ondas Electrolux', 'Micro-ondas 31L com grill e painel touch', 850.00),

('Liquidificador Arno', 'Liquidificador de alta potência com 5 velocidades', 200.00),

('Máquina de Lavar Roupas', 'Lavadora automática de 10kg com painel digital', 1800.00),

('Cafeteira Nespresso', 'Cafeteira automática de cápsulas com 19 bar de pressão', 500.00),

('Purificador de Água', 'Purificador de água com filtro de carvão ativado', 600.00),

('Ar-condicionado Split', 'Ar-condicionado de 12.000 BTUs com controle remoto', 2300.00),

('Bicicleta Aro 29', 'Bicicleta de mountain bike com 21 marchas', 1200.00),

('Máquina de Costura', 'Máquina de costura doméstica com 20 pontos', 900.00);



-- Criação da tabela venda

CREATE TABLE venda (

    id INT AUTO_INCREMENT PRIMARY KEY,

    cliente_id INT,

    data_venda DATE NOT NULL,

    FOREIGN KEY (cliente_id) REFERENCES cliente(id)

);


INSERT INTO venda (cliente_id, data_venda) VALUES

(1, '2024-01-05'),

(2, '2024-01-10'),

(3, '2024-01-15'),

(4, '2024-01-20'),

(4, '2024-01-25'),

(5, '2024-01-30'),

(5, '2024-02-05'),

(1, '2024-02-10'),

(2, '2024-02-15'),

(1, '2024-02-20'),

(1, '2024-02-25'),

(2, '2024-03-01'),

(3, '2024-03-05'),

(4, '2024-03-10'),

(3, '2024-03-15'),

(1, '2024-03-20'),

(6, '2024-03-25'),

(7, '2024-03-30'),

(8, '2024-04-01'),

(9, '2024-04-02'),

(10, '2024-04-03'),

(11, '2024-04-04'),

(12, '2024-04-05'),

(13, '2024-04-06'),

(5, '2024-04-07'),

(1, '2024-04-08');



-- Criação da tabela venda_produto

CREATE TABLE venda_produto (

    venda_id INT NOT NULL,

    produto_id INT NOT NULL,

    quantidade INT NOT NULL,

    FOREIGN KEY (venda_id) REFERENCES venda(id),

    FOREIGN KEY (produto_id) REFERENCES produto(id)

);



INSERT INTO venda_produto (venda_id, produto_id, quantidade) VALUES

(1, 1, 1),

(1, 3, 2),

(2, 4, 1),

(3, 5, 3),

(3, 7, 1),

(4, 6, 2),

(4, 8, 1),

(5, 11, 1),

(6, 10, 1),

(6, 13, 2),

(7, 12, 3),

(7, 14, 1),

(8, 15, 2),

(8, 17, 1),

(9, 16, 1),

(9, 19, 1),

(10, 18, 2),

(10, 20, 3),

(11, 21, 2),

(12, 22, 1),

(12, 24, 1),

(13, 23, 2),

(13, 26, 1),

(14, 25, 3),

(14, 28, 2),

(15, 27, 1),

(15, 29, 2),

(16, 30, 1),

(16, 11, 2),

(17, 19, 1),

(17, 2, 1),

(18, 6, 3),

(19, 5, 2),

(19, 6, 1),

(20, 27, 1),

(21, 29, 2),

(22, 3, 1),

(23, 13, 2),

(24, 23, 1),

(25, 11, 3),

(26, 1, 1);

contando o número de linhas dessas tabelas
SELECT count(*) FROM cliente;
SELECT count(*) FROM produto;

contando o número de linhas em uma tabela usando uma variavel total_vendas
SELECT count(*) AS total_vendas FROM venda;

filtrando todos os clientes que iniciam com o nome joão 
% é usado para ignorar tudo que vem depois de joão o nome para strings
SELECT * FROM cliente
WHERE nome LIKE 'João%';

filtrando os produtos que tem valor menor que 50
SELECT * FROM produto
WHERE preco < 50;

filtrando a quantidade de linhas de produtos que não tem o nome Samsung para strings
SELECT COUNT(*) FROM produto
WHERE nome_produto NOT LIKE '%Samsung%';

filtrando a quantidade de vendas de um cliente especifico para números
SELECT COUNT(*) AS venda_cliente FROM venda_produto
WHERE venda_id = 2;

filtrando todas as vendas que ocorreram até uma data especifica
SELECT count(*) FROM venda
WHERE data_venda <= '2024-03-11';

fazendo uma consulta de todos os nomes dos produtos que foram vendidos pelo id 7
SELECT p.nome_produto
FROM venda_produto vp
JOIN produto p ON vp.produto_id = p.id
WHERE vp.venda_id = 7;

buscando o nome do item mais vendido
SELECT p.nome_produto, SUM(vp.quantidade) AS total_vendido
FROM venda_produto vp
JOIN produto p ON vp.produto_id = p.id
GROUP BY p.nome_produto
ORDER BY total_vendido DESC
LIMIT 1;

consultando o preço total de cada venda
SELECT 
    vp.venda_id,
    SUM(p.preco * vp.quantidade) AS total_venda
FROM 
    venda_produto vp
JOIN 
    produto p ON vp.produto_id = p.id
GROUP BY 
    vp.venda_id
ORDER BY 
    vp.venda_id;

consultando qual o nome do cliente que teve a compra mais cara
SELECT 
    c.nome AS nome_cliente,
    SUM(p.preco * vp.quantidade) AS total_compra
FROM 
    venda_produto vp
JOIN 
    produto p ON vp.produto_id = p.id
JOIN 
    venda v ON vp.venda_id = v.id
JOIN 
    cliente c ON v.cliente_id = c.id
GROUP BY 
    vp.venda_id, c.nome
ORDER BY 
    total_compra DESC
LIMIT 1;
