package teste;

import dao.DAOException;
import dao.persistentebinario.DAO;
import modelo.Pessoa;

public class TestarDAO {

    public static void main(String[] args) {
try {
        // listar pessoas
        DAO dao = new DAO();
        for (Pessoa p : dao.retornarPessoas()){
            System.out.println(p.getNome());
        }
        
        // excluir uma pessoa
        dao.removerPessoaNaPosicao(2);
        } catch (DAOException ex) {
            System.out.println("Erro: " + ex.getMessage());
        }
    }
}
