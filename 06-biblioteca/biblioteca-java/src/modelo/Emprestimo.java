package modelo;

import util.MyDate;

public class Emprestimo {

    Livro livro;
    Usuario usuario;
    MyDate dataEmprestimo;
    MyDate dataDevolucao;
    
    public Emprestimo(Livro l, Usuario u, MyDate dataEmp){
        livro = l;
        usuario = u;
        dataEmprestimo = dataEmp;
    }
    public String toString(){
        return livro+" \n emprestado para: "+usuario+"\n em: "+dataEmprestimo;
    }
    public static void main(String[] args) {
        Livro l = new Livro("Java: como programar (3a edição)",
                "Paul Deitel, Harvel Deitel", 
                "Pearson", "2001");
        Usuario u = new Usuario("123.456.789-10","Jorge");
        Emprestimo emp = new Emprestimo(l, u, new MyDate(01,04,2019));
        System.out.println(emp);
    }
}
