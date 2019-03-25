package teste;

import modelo.Produto;
import modelo.Venda;

public class TestaVenda {

    public static void main(String[] args) {
        
        Venda v = new Venda();
        
        Produto tioUrbano = new Produto();
        tioUrbano.descricao = "Arroz urbano";
        tioUrbano.preco = (float) 3.0;
        tioUrbano.qtdEstoque = 10;
        tioUrbano.unidade = "Pacote";
        
        v.prod = tioUrbano;
        v.qtd = 3;
        
        System.out.println(v);
        
    }
    
}
