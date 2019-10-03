drop database if exists exec_aeroporto;
create database if not exists exec_aeroporto;
use exec_aeroporto;

create table if not exists  passageiro(
	ds_nome varchar(100) not null,
	ds_cpf varchar(15),	
	primary key(ds_cpf)	
);

create table if not exists aviao(
	ds_placa varchar(100) not null,
	ds_nome varchar(100) not null,
	num_cap_max int not null,
	num_tripulacao int not null,
	dom_categoria enum('Primeira Classe', 'Segunda Classe', 'Transporte', 'Etc'),
	num_peso_bag_max float not null,
	ds_nome_emp_resp varchar(100) not null,
	primary key(ds_placa)
);

create table if not exists voo(
	nr_seq_voo int not null AUTO_INCREMENT,
	dt_embarque timestamp not null,
	num_plataforma int not null,
	ds_destino varchar(100) not null,
	ds_placa_aviao varchar(100) not null,
	primary key(nr_seq_voo, ds_placa_aviao),
	foreign key (ds_placa_aviao) references aviao(ds_placa)
);

create table if not exists passageiro_voo(
	ds_cpf_passageiro varchar(15) not null,
	nr_seq_voo	int not null,
	num_peso_bag float not null,
	primary key(ds_cpf_passageiro, nr_seq_voo, num_peso_bag),
	foreign key (nr_seq_voo) references voo(nr_seq_voo),
	foreign key (ds_cpf_passageiro) references passageiro(ds_cpf)
);

insert into passageiro  	values ('Daniel Gripado', '666.666.666-66');
insert into passageiro  	values ('Miguel Gripado', '111.111.111-11');
insert into aviao 			values ('PLACA_DO_BEM', 'Bob', 100, 10, 'Primeira Classe', 100, 'Embratel');
insert into aviao 			values ('PLACA_DO_MAL', 'Marley', 250, 1, 'Etc', 5000, 'Brazzers');
insert into voo				values (null, sysdate(), 666, 'Manaus', 'PLACA_DO_BEM');
insert into voo				values (null, sysdate(), 333, 'Brasília', 'PLACA_DO_MAL');
insert into passageiro_voo	values ('666.666.666-66', 1, 50);
insert into passageiro_voo	values ('111.111.111-11', 1, 50);
insert into passageiro_voo	values ('666.666.666-66', 2, 1000);
insert into passageiro_voo	values ('111.111.111-11', 2, 1000);

select  count(*)
from	passageiro_voo
WHERE	nr_seq_voo = :sequencia_usuario;

select	IF(sum(a.num_peso_bag) > b.num_peso_bag_max, 'Sim', 'Não')
from	passageiro_voo a,
		aviao b
where	a.nr_seq_voo = :nr_seq_voo
group by (sum(a.num_peso_bag))

select IF(cpeso.peso > bout.num_peso_bag_max, 'SIM', 'NÃO')
from (
	select	sum(a.num_peso_bag) peso
	from	passageiro_voo a,
			aviao b,
			voo c
	where	c.nr_seq_voo = :nr_seq_voo
	and		c.nr_seq_voo = a.nr_seq_voo
	and		c.ds_placa_aviao = b.ds_placa
	group by sum(a.num_peso_bag)
	) cpeso,
aviao bout,
passageiro_voo aout,
voo vout
where vout.nr_seq_voo = :nr_seq_voo
and vout.nr_seq_voo = aout.nr_seq_voo
and vout.ds_placa_aviao = bout.ds_placa
group by cpeso.peso;

select d.voo, d.peso, aout.num_peso_bag_max pesomax, if(d.peso > aout.num_peso_bag_max, 'sim', 'não') ultrapassa
from (
select 	
	v.nr_seq_voo voo,	
	sum(pv.num_peso_bag) peso	
FROM	passageiro_voo pv,
		voo v,
		aviao a
where 	pv.nr_seq_voo = v.nr_seq_voo
and		v.ds_placa_aviao = a.ds_placa
group by 	v.nr_seq_voo) d,
	voo vout,
	aviao aout
where d.voo = vout.nr_seq_voo
and aout.ds_placa = vout.ds_placa_aviao;

select o.voo, o.qt_passageiro, a.num_cap_max capacidade_maxima, ((o.qt_passageiro/a.num_cap_max) * 100) percentual_cheio
from (
select nr_seq_voo voo, count(*) qt_passageiro
from passageiro_voo
group by nr_seq_voo
) o,
voo v,
aviao a
where o.voo = v.nr_seq_voo
and v.ds_placa_aviao = a.ds_placa;