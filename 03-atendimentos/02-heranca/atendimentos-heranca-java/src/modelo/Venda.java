package modelo;

public class Venda {

    public Item item;
    public float qtd;

    public Venda(Item i, float quantidadeVendida) {
        this.item = i;
        this.qtd = quantidadeVendida;
        if (i instanceof Produto) {
            Produto p = (Produto) i;
            p.estoque -= quantidadeVendida;
        }
    }

    @Override
    public String toString() {
        String s = "Vendido: " + item + ", qtd=" + qtd;
        if (item instanceof Produto){
            Produto p = (Produto) item;
            s+= ", restou em estoque: "+p.estoque;
        }
        return s;
    }
    
    // teste de venda
    public static void main(String[] args) {   
        // cria uma lâmpada
        Produto p = new Produto();
        p.descricao = "lampada";
        p.unidade = "unidade";
        p.preco = 5;
        p.estoque = 10;
        
        // vende 2 lâmpadas
        Venda v1 = new Venda(p, 2);
        System.out.println(v1);
        
        // vende 4 lâmpadas
        Venda v2 = new Venda(p, 4);
        System.out.println(v2);
    }
}
