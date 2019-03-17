package modelo;

import java.util.Date;

public class Cavalo extends Animal {

    public Cavalo(Date nascimento) {
        super(nascimento);
    }
    @Override
    public void comer() {
        System.out.println("animal mastigando...");
    }
}
