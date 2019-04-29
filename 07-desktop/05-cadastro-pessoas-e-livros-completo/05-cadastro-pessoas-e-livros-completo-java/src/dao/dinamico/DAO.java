package dao.dinamico;

import java.util.ArrayList;
import modelo.Livro;
import modelo.Pessoa;

public class DAO {
    
    // objetos estáticos, para que quaisquer instâncias do DAO
    // acessem os mesmos dados
    static ArrayList<Pessoa> pessoas = new ArrayList();
    static ArrayList<Livro> livros = new ArrayList();
    
    // inicialização do DAO: popular cadastros
    public DAO() {
        // popular o cadastro de livros
        Livro l1 = new Livro ("As regras do trabalho", 
                "Richard Templar", "2010", "Sextante");
        Livro l2 = new Livro("Pense e enriqueça", 
                "Napoleon Hill", "2014", "BestSeller");
        Livro l3 = new Livro("A semente da vitória", 
                "Nuno Cobra", "2001", "Senac SP");
        livros.add(l1);
        livros.add(l2);
        livros.add(l3);
        // popular o cadastro de pessoas
        pessoas.add(new Pessoa("Joao", "Rua 3", "3521-1212", 
                new ArrayList<Livro>() {{ add(l1); }}));
        pessoas.add(new Pessoa("Maria", "Beco Vinte", "4141-1313", 
                new ArrayList<Livro>() {{ add(l2); }}));
        pessoas.add(new Pessoa("Tiago", "Av. Redentor", "não tem", 
                new ArrayList<Livro>() {{ add(l1); add(l3); }}));        
    }
    
    // manipulação de pessoas
    public ArrayList<Pessoa> retornarPessoas() { return pessoas; }
    public void adicionarPessoa(Pessoa p) { pessoas.add(p); }
    public Pessoa retornarPessoa(int i) { return pessoas.get(i); }
    public int retornarQuantidadeDePessoas() { return pessoas.size(); }
    
    // manipulação de livros
    public ArrayList<Livro> retornarLivros() { return livros; }
}
