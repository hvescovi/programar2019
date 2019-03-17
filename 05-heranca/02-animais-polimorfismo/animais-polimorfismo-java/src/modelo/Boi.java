package modelo;

import java.util.Date;

public class Boi extends Animal {

    public Boi(Date nascimento) {
        super(nascimento);
    } 
    @Override
    public void comer() {
        System.out.println("animal ruminando...");
    }    
}
