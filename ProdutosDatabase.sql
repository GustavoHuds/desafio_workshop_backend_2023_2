use estoque;
CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);

CREATE TABLE tipo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    departamentos VARCHAR(255) NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

INSERT INTO produto (nome, valor)
VALUES
    ('Geladeira', 799.99),
    ('Máquina de Lavar', 499.50),
    ('Forno de Micro-ondas', 89.95),
    ('Lava Louças', 349.99),
    ('Cafeteira', 59.99),
    ('Liquidificador', 39.95),
    ('Torradeira', 29.99),
    ('Secador de Cabelo', 49.99),
    ('Ar Condicionado', 799.99),
    ('Aspirador de Pó', 149.95),
    ('Chaleira Elétrica', 39.99),
    ('Forno', 599.99),
    ('Processador de Alimentos', 119.99),
    ('Batedeira', 249.95),
    ('Ferro de Passar', 29.99),
    ('Panela Elétrica de Arroz', 59.95),
    ('Espremedor de Frutas', 49.99),
    ('Forno Elétrico', 69.99),
    ('Prancha de Cabelo', 69.99),
    ('Grelhador Elétrico', 79.95),
    ('Ventilador', 29.99),
    ('Purificador de Ar', 149.99),
    ('Modelador de Cabelo', 34.95),
    ('Fritadeira Elétrica', 49.99),
    ('Batedeira Manual', 24.99),
    ('Ferro de Passar a Vapor', 39.99),
    ('Umidificador', 49.99),
    ('Moedor de Café Elétrico', 29.95),
    ('Panela de Cozimento Lento', 39.99),
    ('Escova de Dentes Elétrica', 49.99),
    ('Liquidificador de Bancada', 79.95),
    ('Barbeador Elétrico', 79.99),
    ('Cozedor a Vapor de Alimentos', 29.99);
    
insert into tipo (departamentos, descricao)
values
	('Eletrodomésticos', 'Produtos eletrodomésticos para sua casa'),
    ('Automotivos', 'Produtos automotivos para o seu carro');
    
select * from produto;
