package util;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class MyDate {
    
    public Date data;
    
    public MyDate(){
        data = new Date();
    }
    public MyDate(int dia, int mes, int ano) {
    // https://stackoverflow.com/questions/48950145/java-8-calculate-months-between-two-dates    
        Calendar c = Calendar.getInstance();
        c.set(Calendar.YEAR, ano); 
        c.set(Calendar.MONTH, mes); 
        c.set(Calendar.DAY_OF_MONTH, dia);
        data = c.getTime();
    }
    public MyDate(Date d) {
        data = d;
    }
    public String toString(){
        // https://www.devmedia.com.br/trabalhando-com-as-classes-date-calendar-e-simpledateformat-em-java/27401
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        return sdf.format(data);
    }
    public int monthsBetween(Date outra){
        Calendar birthDay = new GregorianCalendar();
        birthDay.setTime(this.data);
        Calendar today = new GregorianCalendar(); 
        today.setTime(new Date()); 
        int yearsInBetween = today.get(Calendar.YEAR) - birthDay.get(Calendar.YEAR); 
        int monthsDiff = today.get(Calendar.MONTH) - birthDay.get(Calendar.MONTH); 
        int ageInMonths = yearsInBetween*12 + monthsDiff; 
        return ageInMonths;
    }
}
