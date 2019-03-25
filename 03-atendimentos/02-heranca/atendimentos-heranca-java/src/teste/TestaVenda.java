package teste;

import modelo.Item;
import modelo.Produto;
import modelo.Venda;

public class TestaVenda {

    public static void main(String[] args) {
        
        // cria um produto
        Produto tioUrbano = new Produto();
        tioUrbano.descricao = "Arroz urbano";
        tioUrbano.preco = (float) 3.0;
        tioUrbano.estoque = 6;
        tioUrbano.unidade = "Pacote";
        
        // cria uma venda do produto
        Venda v = new Venda(tioUrbano, 3);
        
        System.out.println(v);
    }
}
