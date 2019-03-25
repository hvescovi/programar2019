package dao.estatico;

import java.util.ArrayList;
import modelo.Atendimento;
import modelo.Cliente;
import modelo.Produto;
import modelo.Servico;
import modelo.Venda;
import util.MyDate;

public class DAO {
    
    public static Atendimento retornarPrimeiroAtendimento(){
        
        Cliente manel = new Cliente();
        manel.cpf = "123.456.789-30";
        manel.nome = "Manoel da Silva";
        
        Servico s = new Servico();
        s.descricao = "Troca de lâmpada";
        s.preco = 10;
        
        Servico s2 = new Servico();
        s2.descricao = "Reparo de tomada";
        s2.preco = 20;
        
        Produto lampada = new Produto();
        lampada.descricao = "Lampada de led";
        lampada.preco = (float) 20.0;
        lampada.qtdEstoque = 20;
        lampada.unidade = "unidade";
        
        Venda v = new Venda();
        v.prod = lampada;
        v.qtd = 2;
        
        Atendimento a1 = new Atendimento(manel);
        a1.data = new MyDate(25,02,2019);
        a1.hora = "21:33";
        //a1.cli = manel;
        a1.servicos.add(s);
        a1.servicos.add(s2);
        a1.vendas.add(v);
        
        return a1;
    }
    
    public static ArrayList<Atendimento> retornarAtendimentos() {
        
        ArrayList<Atendimento> lista = new ArrayList();
        
        Cliente manel = new Cliente();
        manel.cpf = "123.456.789-30";
        manel.nome = "Manoel da Silva";
        
        Servico s = new Servico();
        s.descricao = "Troca de lâmpada";
        s.preco = 10;
        
        Servico s2 = new Servico();
        s2.descricao = "Reparo de tomada";
        s2.preco = 20;
        
        Produto lampada = new Produto();
        lampada.descricao = "Lampada de led";
        lampada.preco = (float) 20.0;
        lampada.qtdEstoque = 20;
        lampada.unidade = "unidade";
        
        Venda v = new Venda();
        v.prod = lampada;
        v.qtd = 2;
        
        Atendimento a1 = new Atendimento(manel);
        a1.data = new MyDate(25,02,2019);
        a1.hora = "21:33";
        //a1.cli = manel;
        a1.servicos.add(s);
        a1.servicos.add(s2);
        a1.vendas.add(v);
        
        lista.add(a1);
        
        //manel.nome = "Joao";
        //lampada.descricao = "Chuveiro";
        //v.prod = lampada;
        
        
        Cliente joao = new Cliente();
        joao.cpf = "123.456.789-30";
        joao.nome = "Joao";
        
        Produto chuveiro = new Produto();
        chuveiro.descricao = "Chuveiro";
        chuveiro.preco = (float) 20.0;
        chuveiro.qtdEstoque = 20;
        chuveiro.unidade = "unidade";
        
        Venda v2 = new Venda();
        v2.prod = chuveiro;
        v2.qtd = 2;
        
        Atendimento a2 = new Atendimento(manel);
        a2.data = new MyDate(20,02,2019);
        a2.hora = "20:33";
        //a1.cli = manel;
        a2.servicos.add(s);
        a2.servicos.add(s2);
        a2.vendas.add(v2);
        
        lista.add(a2);
        
        return lista;
    }
    
}
