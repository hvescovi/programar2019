package modelo;

public class Livro {

   String titulo;
   String autores;
   String editora;
   String ano;
   
   public Livro(String t, String a, String e, String an){
       titulo = t;
       autores = a;
       editora = e;
       ano = an;
   }
   public String toString(){
       return titulo+":"+autores+", "+editora+":"+ano;
   }
   public static void main(String[] args) {
        Livro l = new Livro("Java: como programar (3a edição)",
                "Paul Deitel, Harvel Deitel", 
                "Pearson", "2001");
        System.out.println(l);
   }
}
