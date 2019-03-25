package modelo;

public class Cliente {

    public String cpf;
    public String nome;
    
    public String toString() {
        return cpf+":"+nome;
    }
    
    public static void main(String[] args) {
        
        Cliente manel = new Cliente();
        manel.cpf = "123.456.789-30";
        manel.nome = "Manoel da Silva";
        System.out.println(manel);
    }
}
