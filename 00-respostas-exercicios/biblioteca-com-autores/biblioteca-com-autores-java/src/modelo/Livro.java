package modelo;

import java.util.ArrayList;

public class Livro {

   String titulo;
   ArrayList<Autor> autores;
   String editora;
   String ano;
   
   public Livro(String t, ArrayList<Autor> auts, String e, String an){
       titulo = t;
       autores = auts;
       editora = e;
       ano = an;
   }
   public String toString(){
       return titulo+":"+autores+", "+editora+":"+ano;
   }
   public static void main(String[] args) {
        ArrayList<Autor> au = new ArrayList();
        au.add(new Autor("Paul Deitel"));
        au.add(new Autor("Harvel Deitel"));
        Livro l = new Livro("Java: como programar (3a edição)", 
                au, "Pearson", "2001");
        System.out.println(l);
   }
}
