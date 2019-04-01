package modelo;

public class Aluno extends Usuario {
    
    String matricula;

    public Aluno(String c, String n, String mat) {
        // executa construtor do Usuario
        super(c, n);
        matricula = mat;
    }
    public String toString(){
        // obtém toString to usuario
        return "(aluno)"+super.toString() + ", matrícula: "+matricula;
    }
    public static void main(String[] args) {
        Aluno a= new Aluno("123.456.789-10", "Maria", "201810012");
        System.out.println(a);
    }
}
