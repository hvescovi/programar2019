package modelo;

public class Produto {

    public String descricao;
    public float preco;
    public String unidade;
    public float qtdEstoque;
    
    public String toString(){
        return descricao+": R$ "+preco+
            ", existem: "+qtdEstoque+" "+unidade+"(s)";
    }
}
