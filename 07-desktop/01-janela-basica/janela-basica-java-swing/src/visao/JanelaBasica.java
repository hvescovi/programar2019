package visao;

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class JanelaBasica {

    public static void criar() {
        // criar a janela e configurar tamanho e ação de fechamento
        JFrame j = new JFrame("Janela básica");
        j.setPreferredSize(new Dimension(250, 130));
        j.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // configurar layout da janela
        j.getContentPane().setLayout(new FlowLayout());
        // criar uma mensagem (rótulo)
        JLabel msg = new JLabel("Digite o seu nome: ");
        // adicionar mensagem na janela
        j.getContentPane().add(msg);
        // criar uma caixa de texto e adicionar na janela
        JTextField nome = new JTextField("", 10);
        j.getContentPane().add(nome);
        // criar um botão e adicionar na janela
        JButton b = new JButton("OK");
        j.getContentPane().add(b);
        // criar outro rótulo e adicionar na janela
        JLabel msg2 = new JLabel("");
        j.getContentPane().add(msg2);
        // adicionar um evento ao botão
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0) {
                // colocar o conteúdo da caixa de texto no segundo rótulo
                msg2.setText("Seu nome é: "+nome.getText());
            }
        });
        // exibir a janela
        j.setLocationRelativeTo(null);
        j.pack();
        j.setVisible(true);
    }
    public static void main(String[] args) {
        JanelaBasica.criar();
    }
}