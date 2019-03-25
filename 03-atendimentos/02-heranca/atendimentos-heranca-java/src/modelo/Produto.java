package modelo;

public class Produto extends Item {
    
    public float estoque;
    
    // teste de produto
    public static void main (String args[]){
        Produto p = new Produto();
        p.descricao = "lampada";
        p.unidade = "unidade";
        p.preco = 5;
        p.estoque = 10;
    }
}
