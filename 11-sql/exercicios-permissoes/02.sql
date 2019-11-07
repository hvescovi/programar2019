create DATABASE VENDAS CHARSET latin1 COLLATE latin1_general_cs;
use VENDAS
CREATE table if not exists Pedido(
id_produto varchar (30) not NULL
);
CREATE TABLE cliente(
	ID_CLIENTE INT NOT NULL,
	NOM_CLIENTE VARCHAR(60) NOT NULL,
	CPF_CLIENTE VARCHAR(15)  NOT NULL,
	PRIMARY KEY (ID_CLIENTE)
	);

CREATE TABLE produto(
	ID_PRODUTO INT NOT NULL,
	NOME_PRODUTO VARCHAR(60) NOT NULL,
	PRECO_PRODUTO INT NOT NULL,
	PRIMARY KEY (ID_PRODUTO)
	);


CREATE TABLE pedido(
 	ID_PEDIDO INT NOT NULL,
 	ID_PRODUTO INT NOT NULL,
 	ID_CLIENTE INT NOT NULL,
 	PRIMARY KEY (ID_PEDIDO),
 	FOREIGN KEY (ID_PRODUTO) REFERENCES produto (ID_PRODUTO),
 	FOREIGN KEY (ID_CLIENTE) REFERENCES cliente (ID_CLIENTE)
 	);
 	
	CREATE USER gerente IDENTIFIED BY 'password';
	CREATE USER cliente IDENTIFIED BY 'password';
	CREATE USER vendedor IDENTIFIED BY 'password';

	

\\PERMISSÕES DO VENDEDOR
	GRANT SELECT ON Loja.cliente TO vendedor;
	GRANT SELECT ON Loja.pedido TO vendedor;
	GRANT SELECT ON Loja.produto TO vendedor;

	GRANT INSERT ON Loja.cliente TO vendedor;
	GRANT INSERT ON Loja.pedido TO vendedor;
	

	GRANT UPDATE ON Loja.cliente TO vendedor;
	GRANT UPDATE ON Loja.pedido TO vendedor;
 	

\\PERMISSÕES DO GERENTE
	GRANT DELETE ON Loja.cliente TO gerente;
	GRANT DELETE ON Loja.pedido TO gerente;
	GRANT DELETE ON Loja.produto TO gerente;

	GRANT INSERT ON Loja.cliente TO gerente;
	GRANT INSERT ON Loja.pedido TO gerente;
	GRANT INSERT ON Loja.produto TO gerente;

	GRANT UPDATE ON Loja.cliente TO gerente;
	GRANT UPDATE ON Loja.pedido TO gerente;
 	GRANT UPDATE ON Loja.produto TO gerente;