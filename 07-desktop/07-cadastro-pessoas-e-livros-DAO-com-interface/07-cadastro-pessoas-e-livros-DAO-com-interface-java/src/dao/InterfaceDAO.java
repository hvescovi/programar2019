package dao;

import java.util.ArrayList;
import javax.swing.ListModel;
import modelo.Livro;
import modelo.Pessoa;

public interface InterfaceDAO {
    
    public ArrayList<Pessoa> retornarPessoas();
    public void adicionarPessoa(Pessoa p);
    public Pessoa retornarPessoaAcessoAbsoluto(int i);
    public int retornarQuantidadeDePessoas();
    public void removerPessoaNaPosicao(int posicao);
    public void atualizarPessoa(Pessoa p);
    public boolean existePessoa(String nomeProcurado);    

    public ArrayList<Livro> retornarLivros();
    public Livro buscarLivroPorTitulo(String tit);
    public ArrayList<Livro> retornarLivrosPorTitulosViaModel(ListModel<String> modeloDaLista);
    public ArrayList<Livro> retornarLivrosPorTextoDeBusca(String sequencia);
    public void adicionarLivro(Livro novo);
    public void removerLivro(Livro paraApagar);    
}
