package model;

public class Funcionario {

    public String nome;    
    
    public void dirigir (Carro carro) {
        System.out.println(this.nome+" está dirigindo um "+carro.marca);
    }
   
}
