package dao;

public class DAOException extends Exception {
    
    public DAOException(String msg) {
        super(msg);
    }
    @Override
    public String toString(){
        return "Erro no DAO: "+this.getMessage();
    }
}
