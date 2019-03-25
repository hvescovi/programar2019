package modelo;

public class Servico {
    
    public String descricao;
    public float preco;
    
    public String toString(){
        return descricao+": R$"+preco;
    }
    
    public static void main(String[] args) {
        
        Servico s = new Servico();
        s.descricao = "Troca de lâmpada";
        s.preco = 10;
        System.out.println(s);
    }
}
