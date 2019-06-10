package dao;

import java.util.ArrayList;
import javax.swing.ListModel;
import modelo.Livro;
import modelo.Pessoa;

public interface InterfaceDAO {
    
    public ArrayList<Pessoa> retornarPessoas() throws DAOException ;
    public void adicionarPessoa(Pessoa p) throws DAOException;
    public Pessoa retornarPessoaAcessoAbsoluto(int i) throws DAOException;
    public int retornarQuantidadeDePessoas() throws DAOException;
    public void removerPessoaNaPosicao(int posicao) throws DAOException;
    public void atualizarPessoa(Pessoa p) throws DAOException;
    public boolean existePessoa(String nomeProcurado) throws DAOException;    

    public ArrayList<Livro> retornarLivros() throws DAOException;
    public Livro buscarLivroPorTitulo(String tit) throws DAOException;
    public ArrayList<Livro> retornarLivrosPorTitulosViaModel(ListModel<String> modeloDaLista) throws DAOException;
    public ArrayList<Livro> retornarLivrosPorTextoDeBusca(String sequencia) throws DAOException;
    public void adicionarLivro(Livro novo) throws DAOException;
    public void removerLivro(Livro paraApagar) throws DAOException;    
}
