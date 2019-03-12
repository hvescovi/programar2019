package test;

import model.Carro;
import model.Funcionario;

public class TesteDirecao {
    
    public static void main(String[] args) {
        Carro fox = new Carro();
        Funcionario joao = new Funcionario();
        joao.nome = "Joao";
        fox.marca = "Fox";
        joao.dirigir(fox);
    }
}
