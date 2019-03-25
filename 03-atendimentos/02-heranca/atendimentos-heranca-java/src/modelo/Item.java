package modelo;

public abstract class Item {

    public String descricao;
    public float preco;
    public String unidade;
    
    public String toString(){
        return "item: "+descricao+", preço: R$ "+preco+", unid="+unidade;        
    }
}
