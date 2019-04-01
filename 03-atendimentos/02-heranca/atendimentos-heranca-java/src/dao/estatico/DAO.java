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
        lampada.unidade = "unidade";
        lampada.estoque = 10;
        
        Venda v = new Venda(lampada, 2);
        Venda v2 = new Venda(s, 1);
        Venda v3 = new Venda(s2, 1);
        
        Atendimento a1 = new Atendimento(manel);
        a1.data = new MyDate(25,02,2019);
        a1.hora = "21:33";
        a1.vendas.add(v);
        a1.vendas.add(v2);
        a1.vendas.add(v3);
        
        return a1;
    }
    
    public static ArrayList<Atendimento> retornarAtendimentos() {
        
        ArrayList<Atendimento> lista = new ArrayList();
        
        // obtém primeiro atendimento
        lista.add(retornarPrimeiroAtendimento());
        
        // cria um cliente
        Cliente joao = new Cliente();
        joao.cpf = "123.456.789-30";
        joao.nome = "Joao";
        
        // cria um produto
        Produto chuveiro = new Produto();
        chuveiro.descricao = "Chuveiro";
        chuveiro.preco = (float) 20.0;
        chuveiro.estoque = 20;
        chuveiro.unidade = "unidade";
        
        // cria uma venda
        Venda v2 = new Venda(chuveiro, 3);
        
        // cria um segundo atendimento
        Atendimento a2 = new Atendimento(joao);
        a2.data = new MyDate(20,02,2019);
        a2.hora = "20:33";
        a2.vendas.add(v2);
        
        // adiciona o segundo atendimento
        lista.add(a2);
        
        // o terceiro atendimento ocorrerá sem item (sem custo)
        Atendimento a3 = new Atendimento(joao);
        a3.data = new MyDate(21, 02, 2019);
        a3.hora = "14:00";
        lista.add(a3);
        
        // retorna os 3 atendimentos
        return lista;
    }
    
    // TESTE DO ATENDIMENTO DAO
    public static void main(String[] args) {
             
        System.out.println("*** Teste do método retornarPrimeiroAtendimento");
        System.out.println(DAO.retornarPrimeiroAtendimento());
        
        System.out.println("*** Teste do método retornarAtendimentos");
        for (Atendimento a : DAO.retornarAtendimentos()) {
            System.out.println(a);
        }
    }
}
