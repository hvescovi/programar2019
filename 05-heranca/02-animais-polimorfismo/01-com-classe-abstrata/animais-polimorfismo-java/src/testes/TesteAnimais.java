package testes;

import modelo.Boi;
import modelo.Cavalo;
import util.MyDate;

public class TesteAnimais {
   
    public static void main(String[] args) {        
        Boi b = new Boi((new MyDate(01, 01, 2018)).data);
        Cavalo c = new Cavalo((new MyDate(01, 02, 2018)).data);
        System.out.println(b);
        System.out.println(c);
        b.comer();
        c.comer();
        // boi com mais de 18 meses está apto para o abate
        // https://www.nexojornal.com.br/grafico/2016/12/07/O-tempo-de-vida-dos-animais.-E-o-tempo-de-abate-da-ind%C3%BAstria
        System.out.print("Idade do boi (meses): ");
        System.out.println(b.idadeEmMeses());
    }
}
