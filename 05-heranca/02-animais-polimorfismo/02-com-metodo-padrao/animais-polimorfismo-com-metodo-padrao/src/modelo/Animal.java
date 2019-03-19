package modelo;

import util.MyDate;

public abstract class Animal {

    public MyDate dtNasc;
    
    public void comer() {
        System.out.println("mastigando");
    }
    public Animal() {
        System.out.println("animal criado");
    }
    public Animal(int dia, int mes, int ano) {
        System.out.println("construindo com dados");
    }
}
