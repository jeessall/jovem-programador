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