-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Tempo de geração: 03/10/2019 às 17:52
-- Versão do servidor: 5.7.26
-- Versão do PHP: 7.2.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `aula10bd2`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `Cliente`
--

CREATE TABLE `Cliente` (
  `id` int(11) NOT NULL,
  `nome` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `Cliente`
--

INSERT INTO `Cliente` (`id`, `nome`, `email`) VALUES
(1, 'João de Oliveira', 'joliveira@gmail.com'),
(2, 'Maria de Souza', 'masouza@gmail.com'),
(3, 'Tiago da Silva', 'tisilva@gmail.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Pedido`
--

CREATE TABLE `Pedido` (
  `id` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `Pedido`
--

INSERT INTO `Pedido` (`id`, `id_cliente`, `data`) VALUES
(1, 1, '2019-10-03'),
(2, 3, '2019-10-02');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Produto`
--

CREATE TABLE `Produto` (
  `id` int(11) NOT NULL,
  `nome` varchar(250) NOT NULL,
  `preco` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `Produto`
--

INSERT INTO `Produto` (`id`, `nome`, `preco`) VALUES
(1, 'Bolacha de Maizena 240gr', 3),
(2, 'Mistura para Tapioca 500gr', 5),
(3, 'Coca-cola 300ml lata', 3),
(4, 'Pão de forma multigrãos 500gr', 8);

-- --------------------------------------------------------

--
-- Estrutura para tabela `ProdutoDoPedido`
--

CREATE TABLE `ProdutoDoPedido` (
  `id_pedido` int(11) NOT NULL,
  `id_produto` int(11) NOT NULL,
  `qtd` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `ProdutoDoPedido`
--

INSERT INTO `ProdutoDoPedido` (`id_pedido`, `id_produto`, `qtd`) VALUES
(1, 1, 1),
(2, 1, 5),
(1, 2, 4),
(2, 4, 3);

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `Cliente`
--
ALTER TABLE `Cliente`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `Pedido`
--
ALTER TABLE `Pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Índices de tabela `Produto`
--
ALTER TABLE `Produto`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `ProdutoDoPedido`
--
ALTER TABLE `ProdutoDoPedido`
  ADD PRIMARY KEY (`id_produto`,`id_pedido`),
  ADD KEY `id_pedido` (`id_pedido`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `Cliente`
--
ALTER TABLE `Cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `Pedido`
--
ALTER TABLE `Pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `Produto`
--
ALTER TABLE `Produto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `Pedido`
--
ALTER TABLE `Pedido`
  ADD CONSTRAINT `Pedido_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `Cliente` (`id`);

--
-- Restrições para tabelas `ProdutoDoPedido`
--
ALTER TABLE `ProdutoDoPedido`
  ADD CONSTRAINT `ProdutoDoPedido_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `Produto` (`id`),
  ADD CONSTRAINT `ProdutoDoPedido_ibfk_2` FOREIGN KEY (`id_pedido`) REFERENCES `Pedido` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
