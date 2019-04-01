package modelo;

public class Usuario {

    String cpf;
    String nome;
    
    public Usuario(String c, String n) {
        cpf = c;
        nome = n;
    }
    public String toString(){
        return cpf+":"+nome;
    }
    public static void main(String[] args) {
        Usuario u = new Usuario("123.456.789-10","Jorge");
        System.out.println(u);
    }
}
