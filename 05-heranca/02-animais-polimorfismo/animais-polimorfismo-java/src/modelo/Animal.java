package modelo;

import java.util.Date;
import util.MyDate;

public abstract class Animal {

    private Date dataNascimento;

    public Date getDataNascimento() {
        return dataNascimento;
    }    
    public void setDataNascimento(Date dataNascimento) {
        this.dataNascimento = dataNascimento;
    }    
    public Animal(Date nascimento) {
        this.dataNascimento = nascimento;
    }
    @Override
    public String toString(){
        return "Nascido em: "+(new MyDate(dataNascimento)).toString();
    }
    
    public abstract void comer();
}
