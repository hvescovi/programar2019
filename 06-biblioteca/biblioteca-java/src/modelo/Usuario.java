package modelo;

public abstract class Usuario {

    String cpf;
    String nome;
    
    public Usuario(String c, String n) {
        cpf = c;
        nome = n;
    }
    public String toString(){
        return cpf+":"+nome;
    }
}
