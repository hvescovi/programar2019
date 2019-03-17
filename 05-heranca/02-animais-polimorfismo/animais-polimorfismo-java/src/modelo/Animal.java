package modelo;

import java.util.Date;

public abstract class Animal {

    private Date dataNascimento;

    public Date getDataNascimento() {
        return dataNascimento;
    }    
    public void setDataNascimento(Date dataNascimento) {
        this.dataNascimento = dataNascimento;
    }    
    public Animal(Date nascimento) {
        setDataNascimento(nascimento);
    } 
    
    public abstract void comer();
}
