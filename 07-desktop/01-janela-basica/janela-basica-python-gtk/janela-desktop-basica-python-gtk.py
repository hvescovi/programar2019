import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class JanelaBasica(Gtk.Window):

    def __init__(self):
        # executar inicialização da janela
        Gtk.Window.__init__(self, title="Janela básica")
        # inserir um layout na janela
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(vbox)
        # criar um rótulo na janela
        self.msg = Gtk.Label()
        self.msg.set_label("Nome: ")
        # adicionar o rótulo ao layout
        vbox.pack_start(self.msg, True, True, 0)
        # criar uma caixa de texto e adicionar à janela
        self.nome = Gtk.Entry()
        vbox.pack_start(self.nome, True, True, 0)
        # criar um botão
        self.button = Gtk.Button(label="Ok")
        # associar evento de clique ao botão
        self.button.connect("clicked", self.on_button_clicked)
        # adicionar botão à janela
        vbox.pack_start(self.button, True, True, 0)
        # adicionar outro rótulo
        # criar um rótulo na janela
        self.msg2 = Gtk.Label()
        self.msg2.set_width_chars(20)
        #self.msg2.set_label(" ")
        # adicionar o rótulo ao layout
        vbox.pack_start(self.msg2, True, True, 0)        

    #  evento de clique no botão
    def on_button_clicked(self, widget):
        # colocar no segundo rótulo o conteúdo da caixa de texto
        self.msg2.set_label("Seu nome é: "+self.nome.get_text())

# instanciação da janela     
win = JanelaBasica()
# quebra do loop do gtk ao fechar a janela (encerramento do programa)
win.connect("destroy", Gtk.main_quit)
# centralização da janela
win.set_position(Gtk.WindowPosition.CENTER)
# exibição da janela
win.show_all()
# início do gtk (loop contínuo)
Gtk.main()