CREATE SCHEMA primeira_aula CHARACTER SET latin1 COLLATE latin1_general_cs;

USE primeira_aula;

create table passageiro (
	cpf float(11,0) primary key,
	nome varchar(255)
);

create table voo(
	id int AUTO_INCREMENT primary key,
	embarque datetime,
	plataforma int(6),
	destino varchar(255)
);

create table aviao(
	id int AUTO_INCREMENT primary key,
	nome varchar(255),
	qtdmax int(7),
	qtdtrip int(3),
	categoria varchar(255),
	pesomax int(11),
	empres varchar(255)
);

create table bagagem(
	codigo varchar(255) PRIMARY KEY,
	cpfpas float(11,0),
	voopas int(11),
	pesbag float (7,2),
	foreign key (cpfpas) REFERENCES passageiro(cpf),
	foreign key (voopas) REFERENCES voo(id)
);

insert into passageiro values 
	(02198309821, 'Lucas'),
	(02198342241, 'zé'),
	(02124234311, 'joão'),
	(98149871421, 'thiago'),
	(21988156131, 'nicolas'),
	(23165131221, 'leandro'),
	(56465465465, 'bla-ir'),
	(99999999999, 'Ble-n-zo');

insert into voo values 
	( Null, '1000-01-01', 1, 'Bahia'),
	( Null, '2000-01-01', 2, 'Boston'),
	( Null, '3000-01-01', 3, 'Pernambuco'),
	( Null, '4000-01-01', 4, 'Aracaju'),
	( Null, '6000-01-01', 6, 'Kelvin'),
	( Null, '7000-01-01', 7, 'Hawai'),
	( Null, '8000-01-01', 8, 'Arapongas');

insert into aviao values 
	( Null, 'AVIBLA', 150, 8, 'PRIMEIRA-CLASSE', 12000, 'Bahia C.A.'),
	( Null, 'AVIBLE', 200, 10, 'SEGUNDA-CLASSE', 18000, 'Bahia C.A.'),
	( Null, 'AVIBLI', 250, 14, 'LIXÃO', 12000, 'Bahia C.A.');


insert into bagagem values
	('aaa', 02198309821, 1, 25),
	('bbb', 02198342241, 2, 15),
	('ccc', 02124234311, 3, 10),
	('ddd', 98149871421, 4, 8),
	('eee', 21988156131, 6, 18),
	('fff', 23165131221, 7, 20),
	('ggg', 56465465465, 2, 46),
	('hhh', 99999999999, 1, 80);

alter table voo add column avivoo int(11);
alter table voo add constraint voo_aviao foreign key(avivoo)
references aviao(id);

update voo set avivoo=3 where id < 8;
update voo set avivoo=2 where id < 4;
update voo set avivoo=1 where id < 2;
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------

-- QUANTAS PESSOAS ESTÃO EM UM DETERMINADO VOO?

select 
	count(distinct bagagem.cpfpas) 'qtd pessoas', 
	voopas 
from 
	bagagem 
where 
	voopas = 1 
group by 
	voopas;

-- O PESO DAS BAGAGENS SERÁ SUPORTADO PELO AVIÃO?

select 
	IF(sum(bagagem.pesbag) > aviao.pesomax, "Não", "sim") 'Aguenta o peso?',
	aviao.id 'com o avião'
from 
	bagagem, voo, aviao 
where 
	bagagem.voopas = voo.id and
	voo.avivoo = aviao.id 
group by 
	aviao.id;

-- QUAL A PERCENTAGEM DE LOTAÇÃO DO VOO ? 

select 
	count(codigo) 'pessoas', 
	voopas 'voo', 
	aviao.qtdmax 'total', 
	count(codigo)*100/aviao.qtdmax'%' 
from 
	bagagem, voo, aviao 
where 
	bagagem.voopas = voo.id and
	voo.avivoo = aviao.id 
group by 
	voopas;

