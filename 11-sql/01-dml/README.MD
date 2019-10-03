* AULA 10 BD2 (03/10/2019)

a) mostrar tudo
select * from ProdutoDoPedido pp, Pedido pe, Produto po
where pp.id_pedido=pe.id and pp.id_produto=po.id

b) mostrar tudo (com inner join)
select * from ProdutoDoPedido pp
inner join Pedido pe on pp.id_pedido=pe.id
inner join Produto po on pp.id_produto=po.id

c) produtos que estão nos pedidos
select distinct nome from Produto po
inner join ProdutoDoPedido pp on pp.id_produto=po.id

d) produtos e em quais pedidos esses produtos se encontram
select * from Produto po
left join ProdutoDoPedido pp on pp.id_produto=po.id

e) produtos que que não estão em nenhum pedido
select nome from Produto po
left join ProdutoDoPedido pp on pp.id_produto=po.id
where pp.id_produto IS NULL

f) clientes e produtos comprados
select cli.nome, po.nome from Cliente cli
inner join Pedido pe on pe.id_cliente = cli.id
inner join ProdutoDoPedido pp on pp.id_pedido = pe.id
inner join Produto po on pp.id_produto = po.id

tarefas: 
- listar produtos que nenhum cliente comprou ainda
- quantos produtos cada cliente comprou

entregar todas as ações no seu github (fornecer o link na planilha compartilhada)

