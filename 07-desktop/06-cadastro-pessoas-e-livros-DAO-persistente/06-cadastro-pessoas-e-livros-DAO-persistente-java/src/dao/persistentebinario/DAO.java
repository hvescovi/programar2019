package dao.persistentebinario;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import javax.swing.ListModel;
import modelo.Livro;
import modelo.Pessoa;

public class DAO implements Serializable {

    // configuração específica do DAO dump binário:
    String caminhoArquivo = "/home/friend/dados.bin";

    // variáveis para uso *** interno e temporário *** do DAO
    ArrayList<Pessoa> pessoas = new ArrayList();
    ArrayList<Livro> livros = new ArrayList();

    // inicialização do DAO: popular cadastros, se arquivo não existir
    public DAO() {
        Path path = Paths.get(caminhoArquivo);
        if (!Files.exists(path)) {
            popularDados();
        }
    }

    // método auxiliar: popular dados
    void popularDados() {
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

        // gravar
        salvarDadosNoDisco(pessoas, livros);
    }

    // método auxiliar: carregar dados do disco
    HashMap carregarDadosDoDisco() {
        // objetos auxiliares temporários
        pessoas = new ArrayList();
        livros = new ArrayList();
        // preparar o retorno
        HashMap ret = new HashMap();
        try {
            // ler o arquivo
            FileInputStream fis = new FileInputStream(caminhoArquivo);
            ObjectInputStream ois = new ObjectInputStream(fis);
            // converter o conteúdo lido nos objetos
            // ler pessoas e depois livros (mesma ordem de gravação)
            pessoas = (ArrayList<Pessoa>) ois.readObject();
            livros = (ArrayList<Livro>) ois.readObject();
            // captura de diversos tipos de erros possíveis    
        } catch (FileNotFoundException fex) {
            fex.printStackTrace();
        } catch (IOException ioex) {
            ioex.printStackTrace();
        } catch (ClassNotFoundException cex) {
            cex.printStackTrace();
        }
        // adicionar dados ao retorno
        ret.put("pessoas", pessoas);
        ret.put("livros", livros);
        // retornar :-)
        return ret;
    }

// método auxiliar para gravar dados no disco
    void salvarDadosNoDisco(ArrayList<Pessoa> ps, ArrayList<Livro> ls) {
        try {
            // prepara ponteiro de gravação
            FileOutputStream fos = new FileOutputStream(caminhoArquivo);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            // grava pessoas e depois livros
            oos.writeObject(ps);
            oos.writeObject(ls);
            // fecha o arquivo e efetiva a gravação
            oos.close();
            // tratamento de possível erro de I/O
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    // manipulação de pessoas
    public ArrayList<Pessoa> retornarPessoas() {
        // carregar os dados
        HashMap tmp = carregarDadosDoDisco();
        // retorna as pessoas
        return (ArrayList<Pessoa>) tmp.get("pessoas");
    }

    public void adicionarPessoa(Pessoa p) {
        // carregar os dados
        HashMap dados = carregarDadosDoDisco();
        pessoas = (ArrayList<Pessoa>) dados.get("pessoas");
        livros = (ArrayList<Livro>) dados.get("livros");
        // adicionar a pessoa
        pessoas.add(p);
        // atualizar dados no disco
        salvarDadosNoDisco(pessoas, livros);
    }

    public Pessoa retornarPessoaAcessoAbsoluto(int i) {
        // carregar as pessoas
        pessoas = (ArrayList<Pessoa>) (carregarDadosDoDisco()).get("pessoas");
        return pessoas.get(i);
    }

    public int retornarQuantidadeDePessoas() {
        pessoas = (ArrayList<Pessoa>) (carregarDadosDoDisco()).get("pessoas");
        return pessoas.size();
    }

    // *********************
    // manipulação de livros
    // *********************
    // obter  livros
    public ArrayList<Livro> retornarLivros() {
        // carrega os dados
        HashMap tmp = carregarDadosDoDisco();
        // retorna os livros
        return (ArrayList<Livro>) tmp.get("livros");
    }

    public Livro buscarLivroPorTitulo(String tit) {
        // carregar os livros
        livros = (ArrayList<Livro>) (carregarDadosDoDisco()).get("livros");
        for (Livro livro : livros) {
            if (livro.getTitulo().equals(tit)) {
                return livro;
            }
        }
        return new Livro("nao encontrado", "nao encontrado", "nao encontrado", "nao encontrado");
    }

    public ArrayList<Livro> retornarLivrosPorTitulosViaModel(ListModel<String> modeloDaLista) {
        // carregar os livros
        livros = (ArrayList<Livro>) (carregarDadosDoDisco()).get("livros");
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
        // carregar os dados
        HashMap dados = carregarDadosDoDisco();
        pessoas = (ArrayList<Pessoa>) dados.get("pessoas");
        livros = (ArrayList<Livro>) dados.get("livros");
        // remover a pessoa
        pessoas.remove(posicao - 1);
        // atualizar dados no disco
        salvarDadosNoDisco(pessoas, livros);
    }

    // ESSE MÉTODO NÃO ATUALIZA O NOME DA PESSOA,
    // pois essa é a chave de busca
    public void atualizarPessoa(Pessoa p) {
        // carregar os dados
        HashMap dados = carregarDadosDoDisco();
        pessoas = (ArrayList<Pessoa>) dados.get("pessoas");
        livros = (ArrayList<Livro>) dados.get("livros");
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
            // atualizar dados no disco
            salvarDadosNoDisco(pessoas, livros);
        }
    }

    public ArrayList<Livro> retornarLivrosPorTextoDeBusca(String sequencia) {
        // carregar os livros
        livros = (ArrayList<Livro>) (carregarDadosDoDisco()).get("livros");
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
        // carregar os dados
        HashMap dados = carregarDadosDoDisco();
        pessoas = (ArrayList<Pessoa>) dados.get("pessoas");
        livros = (ArrayList<Livro>) dados.get("livros");
        // adicionar o livro
        livros.add(novo);
        // atualizar os dados
        salvarDadosNoDisco(pessoas, livros);
    }

    public void removerLivro(Livro paraApagar) {
        // carregar os dados
        HashMap dados = carregarDadosDoDisco();
        pessoas = (ArrayList<Pessoa>) dados.get("pessoas");
        livros = (ArrayList<Livro>) dados.get("livros");
        // excluir o livro
        livros.remove(paraApagar);
        // atualizar os dados
        salvarDadosNoDisco(pessoas, livros);
    }

    public boolean existePessoa(String nomeProcurado) {
        // carregar os dados
        HashMap dados = carregarDadosDoDisco();
        pessoas = (ArrayList<Pessoa>) dados.get("pessoas");
        livros = (ArrayList<Livro>) dados.get("livros");
        // busca a pessoa pelo nome
        for (Pessoa p : pessoas) {
            if (p.getNome().equals(nomeProcurado)) {
                return true;
            }
        }
        // não achou? retorna falso
        return false;
    }

}
