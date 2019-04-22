package modelo;

public class Livro {
    
    private String titulo;
    private String autores;
    private String ano;
    private String editora;

    public String getTitulo() { return titulo; }
    public void setTitulo(String t) { titulo = t; }
    public String getAutores() { return autores; }
    public void setAutores(String a) { autores = a; }
    public String getAno() { return ano; }
    public void setAno(String a) { ano = a; }
    public String getEditora() { return editora; }
    public void setEditora(String e) {editora = e; }
    // redefinindo construtor que informa parâmetros
    public Livro(String tit, String aut, String an, String ed){
        titulo = tit; autores = aut; ano = an; editora = ed;
    }
    
}
