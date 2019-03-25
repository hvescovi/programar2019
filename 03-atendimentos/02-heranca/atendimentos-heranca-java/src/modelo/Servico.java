package modelo;

public class Servico extends Item {
    
    // teste de serviço
    public static void main(String[] args) {
        Servico s = new Servico();
        s.descricao = "Troca de lâmpada";
        s.preco = 10;
        s.unidade = "hora";
        System.out.println(s);
    }
}
