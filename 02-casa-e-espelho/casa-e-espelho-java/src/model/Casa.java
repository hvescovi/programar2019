package model;

public class Casa {
    public int quartos;
    public String cor;
    public Espelho esp;

    public String toString(){
        String s = "Casa de "+quartos+
                " quartos, "+cor;
        if (esp != null) {
            s += ", com espelho de "+
                esp.altura+" por "+esp.largura
                    +" (centímetros)";
        }
        return s;
    }
    public static void main(String[] args) {
        Espelho e = new Espelho();
        e.altura = 20;
        e.largura = 30;
        Casa c = new Casa();
        c.quartos = 3;
        c.cor = "azul";
        c.esp = e;
        System.out.println(c);
    }
}
