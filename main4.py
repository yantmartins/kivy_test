from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout ##BoxLayout é uma caixa que irá conter os WIDGETS

class Programa(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        
        self.texto = Label(text='0', font_size='50px')
        self.botao = Button(text='+',font_size='50px')
        self.botaominus = Button(text='-',font_size='50px')

        
        self.botao.bind(on_press = self.add)
        self.botaominus.bind(on_press=self.subtract)

        
        layout.add_widget(self.botao)
        layout.add_widget(self.texto)
        layout.add_widget(self.botaominus)

        return layout
    
    def add(self,event):
        self.texto.text = str(int(self.texto.text)+1)
    def subtract(self, event):
        self.texto.text = str(int(self.texto.text) - 1)

if __name__ == "__main__":
    Programa().run()  ## INSTANCIA A CLASSE E CHAMA O METODO RUN DE APP
