package teste;

import modelo.Aluno;
import modelo.AreaDeAtuacao;
import modelo.Docente;
import modelo.Periodico;
import modelo.ProjetoIntegrador;

public class TestarPI {
    
public static void main(String[] args) {
Aluno a1 = new Aluno();
a1.nome = "João da Silva";    
a1.turma = "tecinfointegrado 301";

Docente d1 = new Docente();
d1.nome = "Paulo Oliveira";

AreaDeAtuacao sd = new AreaDeAtuacao();
sd.nome = "Sistemas Distribuídos";

Periodico p = new Periodico();
p.titulo = "Journal of Systems Architecture";
p.sigla = "JSA";
p.editora = "Elsevier";
p.ISSN = "1383-7621";

sd.ondePublicar.add(p);
d1.areas.add(sd);

ProjetoIntegrador pi=new ProjetoIntegrador();
pi.titulo = "Influência da baba das formigas"
        + " na rachadura das calçadas";
pi.ano = "2019";
pi.alunos.add(a1);
pi.orientadores.add(d1);

System.out.println(pi.titulo+", "+pi.ano);
}    
}
