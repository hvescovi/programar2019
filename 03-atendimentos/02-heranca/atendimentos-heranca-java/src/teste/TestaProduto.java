package teste;

import modelo.Produto;

public class TestaProduto {

    public static void main(String[] args) {
        
        Produto tioUrbano = new Produto();
        tioUrbano.descricao = "Arroz urbano";
        tioUrbano.preco = (float) 3.0;
        tioUrbano.estoque = 6;
        tioUrbano.unidade = "Pacote";
        
        System.out.println(tioUrbano);                
    }
}
