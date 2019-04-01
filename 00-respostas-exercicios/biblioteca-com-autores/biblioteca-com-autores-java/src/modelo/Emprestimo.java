package modelo;

import java.util.ArrayList;
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
        ArrayList<Autor> au = new ArrayList();
        au.add(new Autor("Paul Deitel"));
        au.add(new Autor("Harvel Deitel"));
        Livro l = new Livro("Java: como programar (3a edição)", 
                au, "Pearson", "2001");
        Aluno a= new Aluno("123.456.789-10", "Maria", "201810012");
        Emprestimo emp = new Emprestimo(l, a, new MyDate(01,04,2019));
        System.out.println(emp);
    }
}
