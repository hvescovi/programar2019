package dao.dinamico;

import java.util.ArrayList;
import javax.swing.ListModel;
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
        Livro l1 = new Livro("As regras do trabalho",
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
                new ArrayList<Livro>() {
            {
                add(l1);
            }
        }));
        pessoas.add(new Pessoa("Maria", "Beco Vinte", "4141-1313",
                new ArrayList<Livro>() {
            {
                add(l2);
            }
        }));
        pessoas.add(new Pessoa("Tiago", "Av. Redentor", "não tem",
                new ArrayList<Livro>() {
            {
                add(l1);
                add(l3);
            }
        }));
    }

    // manipulação de pessoas
    public ArrayList<Pessoa> retornarPessoas() {
        return pessoas;
    }

    public void adicionarPessoa(Pessoa p) {
        pessoas.add(p);
    }

    public Pessoa retornarPessoaAcessoAbsoluto(int i) {
        return pessoas.get(i);
    }

    public int retornarQuantidadeDePessoas() {
        return pessoas.size();
    }

    // manipulação de livros
    public ArrayList<Livro> retornarLivros() {
        return livros;
    }

    public Livro buscarLivroPorTitulo(String tit) {
        for (Livro livro : livros) {
            if (livro.getTitulo().equals(tit)) {
                return livro;
            }
        }
        return new Livro("nao encontrado", "nao encontrado", "nao encontrado", "nao encontrado");
    }

    public ArrayList<Livro> retornarLivrosPorTitulosViaModel(ListModel<String> modeloDaLista) {
        // prepara o retorno
        ArrayList<Livro> retorno = new ArrayList();
        // percorre os títulos
        for (int i = 0; i < modeloDaLista.getSize(); i++) {
            // busca o livro pelo titulo
            Livro tmp = buscarLivroPorTitulo(modeloDaLista.getElementAt(i));
            // inclui na lista de retorno
            retorno.add(tmp);
        }
        return retorno;
    }

    public void removerPessoaNaPosicao(int posicao) {
        pessoas.remove(posicao - 1);
    }

    // ESSE MÉTODO NÃO ATUALIZA O NOME DA PESSOA,
    // pois essa é a chave de busca
    public void atualizarPessoa(Pessoa p) {
        // sinaliza que será feita uma busca
        int ondeMudar = -1;
        // busca a pessoa pelo nome
        for (int i = 0; i < pessoas.size(); i++) {
            if (pessoas.get(i).getNome().equals(p.getNome())) {
                ondeMudar = i;
                break;
            }
        }
        // se achou a pessoa pra mudar
        if (ondeMudar >= 0) {
            pessoas.set(ondeMudar, p);
        }
    }

    public ArrayList<Livro> retornarLivrosPorTextoDeBusca(String sequencia) {
        // criar lista de retorno
        ArrayList<Livro> retorno = new ArrayList();
        // converter string de busca para minúsculas
        sequencia = sequencia.toLowerCase();
        // buscar nos livros a sequência de busca
        for (Livro livro : livros) {
            // livro convertido para minúsculas
            Livro tmp = new Livro(livro.getTitulo().toLowerCase(),
                    livro.getAutores().toLowerCase(),
                    livro.getAno().toLowerCase(),
                    livro.getEditora().toLowerCase());
            // se o livro atual possui algo da string de busca
            if (tmp.getTitulo().contains(sequencia)
                    || tmp.getAutores().contains(sequencia)
                    || tmp.getAno().contains(sequencia)
                    || tmp.getEditora().contains(sequencia)) {
                // adiciona o livro no retorno
                retorno.add(livro);
            }
        }
        return retorno;
    }

    public void adicionarLivro(Livro novo) {
        livros.add(novo);
    }

    public void removerLivro(Livro paraApagar) {
        livros.remove(paraApagar);
    }

}
