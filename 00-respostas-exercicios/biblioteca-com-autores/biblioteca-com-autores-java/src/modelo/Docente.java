package modelo;

public class Docente extends Usuario {
    
    String siape;

    public Docente(String c, String n, String mat) {
        // executa construtor do Usuario
        super(c, n);
        siape = mat;
    }
    public String toString(){
        // obtém toString to usuario
        return "(docente)"+super.toString() + ", siape: "+siape;
    }
    public static void main(String[] args) {
        Docente d= new Docente("123.456.789-10", "Teresa", "1510001");
        System.out.println(d);
    } 
}
