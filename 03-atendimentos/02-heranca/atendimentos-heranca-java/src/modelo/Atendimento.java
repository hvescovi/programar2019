package modelo;

import dao.estatico.DAO;
import java.util.ArrayList;
import util.MyDate;

public class Atendimento {

    public MyDate data;
    public String hora;
    public Cliente cli;
    public ArrayList<Venda> vendas = new ArrayList();
    
    // não é possível haver atendimento sem cliente
    public Atendimento(Cliente c) {
        this.cli = c;
    }
    
    public String toString(){
        
        String s = data+ " às "+hora + "; atendido: "+cli;
        
        for (Venda v : vendas){
            s+= "\n"+v;
        }
        
        s+= "\nTotal: "+ Total();
        
        return s;
    }
    
    public float Total() {
        float total = 0;
        // percorre as vendas (serviços e/ou produtos)
        for (Venda v : vendas){
            // acumula o total do item
            total += (v.item.preco)*(v.qtd);
        }
        return total;
    }
    
    
}
