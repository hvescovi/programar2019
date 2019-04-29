package modelo;

import java.util.ArrayList;

public class Pessoa {
    private String nome;
    private String endereco;
    private String telefone;
    ArrayList<Livro> livros = new ArrayList();

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }
    public String getEndereco() { return endereco; }
    public void setEndereco(String e) {endereco = e; }
    public String getTelefone() { return telefone; }
    public void setTelefone(String t) {telefone = t; }
    // construtor
    public Pessoa(String n, String e, String t, ArrayList<Livro> livros) {
        nome = n; endereco = e; telefone = t; this.livros = livros; }
    public ArrayList<Livro> getLivros(){ return livros; }
}