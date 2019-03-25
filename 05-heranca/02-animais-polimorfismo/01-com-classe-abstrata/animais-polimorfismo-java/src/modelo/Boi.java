package modelo;

import java.util.Date;
import util.MyDate;

public class Boi extends Animal {

    public int idadeEmMeses(){
        MyDate m = new MyDate(getDataNascimento());
        return m.monthsBetween(new Date());
    }
    @Override
    public void comer() {
        System.out.println("animal ruminando...");
    }    
    @Override
    public String toString(){
        return "Boi " + super.toString();
    }    
}
