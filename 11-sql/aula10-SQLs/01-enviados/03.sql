CREATE DATABASE aeroporto CHARSET latin1 COLLATE latin1_general_cs;

use aeroporto;

create table if not exists aviao (
	nr_sequencia integer primary key,
	qt_capacidade_peso float,
	qt_capacidade_pessoa integer
);

create table if not exists voo (
	nr_sequencia integer primary key,
	nr_seq_aviao integer,
	foreign key (nr_seq_aviao) references aviao (nr_sequencia)
);

create table if not exists passageiro (
	nr_sequencia integer primary key,
	nm_passageiro varchar(30),
	nr_seq_voo integer,
	foreign key (nr_seq_voo) references voo (nr_sequencia)
);

create table if not exists bagagem (
	nr_sequencia integer primary key,
	cd_bagagem varchar(5),
	qt_peso float,
	nr_seq_passageiro integer,
	foreign key (nr_seq_passageiro) references passageiro (nr_sequencia)
);

insert into aviao values (1, 1000, 50);
insert into voo values (1, 1);
insert into passageiro values (1, 'joao', 1);
insert into passageiro values (2, 'maria', 1);
insert into passageiro values (3, 'nicolas', 1);
insert into bagagem values (1, 'AN6Y4B', 50.0, 1);
insert into bagagem values (2, 'AN6Y4C', 50.0, 1);
insert into bagagem values (3, 'AN1X4D', 150.0, 2);
insert into bagagem values (4, 'AN2Y4B', 2.0, 3);


select count(1)
from passageiro
where nr_seq_voo = 1;

select COALESCE(max('S'), 'N')
from aviao a, voo b, passageiro c, bagagem d
where a.nr_sequencia = b.nr_seq_aviao
and b.nr_sequencia = c.nr_seq_voo
and c.nr_sequencia = d.nr_seq_passageiro
and a.qt_capacidade_peso >= ( 	select count(qt_peso)
			 	from bagagem z
				where z.nr_sequencia = d.nr_sequencia	);
								
select count(a.nr_sequencia) * 100 / c.qt_capacidade_pessoa
from passageiro a, voo b, aviao c
where b.nr_sequencia = a.nr_seq_voo
and c.nr_sequencia = b.nr_seq_aviao
group by c.qt_capacidade_pessoa;
		
